#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2014-4-2

@author: Wenjun Hu
'''

# Global import
import logging, os

# Androguard import
#from androguard.core.bytecode import *
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.bytecodes.apk import APK
from androguard.core.analysis.analysis import VMAnalysis

# PermissionSanner import
from application.application import *
from util.util import *
from permissions_map.permissions import PERMISSIONS

# Logger
LOG_FILE = r'log.txt'
log = logging.getLogger('log')
log.setLevel(logging.INFO)
formatter = logging.Formatter('[%(asctime)s %(levelname)s] %(message)s')
handler = logging.StreamHandler(open(LOG_FILE, 'a', 0))
handler.setFormatter(formatter)
log.addHandler(handler)


class PermissionScanner():
    def __init__(self, apk_file, extract_string=False):
        self.__apk_file = apk_file
        
        self.__apk = None
        self.__unclaimed_permissions = []

        
    def start_analysis(self):
        try:
            if not os.path.exists(self.__apk_file):
                log.warn("%s not exists" % self.__apk_file)
                return
            
            # Create APK instance
            try:
                self.__apk = APK(self.__apk_file, raw=False)
            except Exception, ex:
                log.exception(ex)
                return
        
            if self.__apk == None:
                log.error('Fail to create APK instance')
                return
            
            # Analyze unclaimed permissions
            log.info('Start analyzing %s...' % self.__apk_file)
            self.__unclaimed_permissions = self.__analyze_apk(self.__apk)
            
            # Analysis done
            log.info('Analysis for %s done' % self.__apk_file)
        except Exception, ex:
            log.exception(ex)

        
    def __analyze_apk(self, apk, raw=False):
        unclaimed_permissions = []
        
        # Create VMAnalysis instance
        try:
            vm_analysis = self.__analyze_dex(apk.get_dex(), raw=True)
        except Exception, ex:
            log.exception(ex)
            return unclaimed_permissions
        
        # Perform analysis
        try:
            unclaimed_permissions = self.__perform_analysis(apk, vm_analysis)
        except Exception, ex:
            log.exception(ex)
            return unclaimed_permissions
        
        return unclaimed_permissions
        
    
    def __analyze_dex(self, dex_file, raw=False) :
        # DalvikVMFormat
        dalvik_vm_format = None
        if raw == False :
            dalvik_vm_format = DalvikVMFormat( open(dex_file, "rb").read() )
        else :
            dalvik_vm_format = DalvikVMFormat( dex_file )
      
        # VMAnalysis
        vm_analysis = VMAnalysis( dalvik_vm_format )
        dalvik_vm_format.set_vmanalysis( vm_analysis )
                
        return vm_analysis
    
    def __perform_analysis(self, apk, vm_analysis):
        # Get permissions and remove duplicate ones
        manifest_permissions = set(apk.get_permissions())
        all_permissions = set(PERMISSIONS)
        manifest_permissions = list(all_permissions & manifest_permissions)
        
        used_permissions = []
        
        # Get manifest intents
        manifest_intents = get_manifest_intents(apk)
        
        # Search APIs
        for tainted_package,_ in vm_analysis.tainted_packages.get_packages():
            paths = tainted_package.get_methods()
            class_name = tainted_package.get_name()
            for path in paths:
                api_tuple = (class_name, path.get_name())
                permission = get_permission_by_api(api_tuple)
                if permission:
                    used_permissions.append(permission)
            
        # If need search string
        if(len(used_permissions) != (len(manifest_permissions))):
            # Search strings
            for s, _ in vm_analysis.tainted_variables.get_strings() :
                string_info = s.get_info()
                permission = get_permission_by_intent(string_info)
                if not permission:
                    permission = get_permission_by_contentprovider(string_info)
                if permission:
                    used_permissions.append(permission)
                    
        # If need search manifest intents
        if(len(used_permissions) != (len(manifest_permissions))):
            for intent in manifest_intents:
                permission = get_permission_by_intent(intent)
                if permission:
                    used_permissions.append(permission)
                    
        unclaimed_permissions = list(set(manifest_permissions) - set(used_permissions))
                
        return unclaimed_permissions
    
    def get_unclaimed_permissions(self):
        """
            @rtype : a list of strings
        """
        return self.__unclaimed_permissions

# Run
if __name__ == '__main__':
    test_apk = r'test.apk'
    # Create PermissionScanner instance
    
    permission_scanner = PermissionScanner(test_apk, extract_string=True)
    
    # start analyze
    permission_scanner.start_analysis()

    # Get unclamed permissions
    print 'unclaimed permissions:', permission_scanner.get_unclaimed_permissions()
        
        
            
            
        
    
        
        
        
        




    