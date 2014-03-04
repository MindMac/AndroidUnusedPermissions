#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2014-3-2

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
    def __init__(self, apk_file):
        self.__apk_file = apk_file
        self.__apk = None
        self.__unclaimed_permissions = []
        self.__certifiacte_info = {}
        
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
            
            # Get certificate information
            log.info('Extract certificate information')
            self.__certifiacte_info = get_certificate_information(self.__apk)
            
            # Analysis done
            log.info('Analysis for %s done' % self.__apk_file)
        except Exception, ex:
            log.exception(ex)
            
    def get_unclaimed_permissions(self):
        """
            @rtype : a list of strings
        """
        return self.__unclaimed_permissions
    
    def get_certificate_info(self):
        """
            @rtype: a dictionary {'issuer':'' , 'subject':'' , 'serial_num':'', 'thumbprint':''}
        """
        return self.__certifiacte_info

        
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
        permissions = set(apk.get_permissions())
        all_permissions = set(PERMISSIONS)
        permissions = list(all_permissions & permissions)
        
        unclaimed_permissions = permissions
        
        # Get manifest intents
        manifest_intents = get_manifest_intents(apk)
        
        for permission in permissions:
            searched = False
            try:
                # Search method
                class_method_tuple_list = get_api_list(permission)
                if class_method_tuple_list:
                    for class_method_tuple in class_method_tuple_list:
                        searched = search_method(vm_analysis, class_method_tuple[0], class_method_tuple[1])
                        if searched:
                            unclaimed_permissions.remove(permission)
                            break
                    
                # Search intent
                intent_list = get_intent_list(permission)
                if intent_list:
                    for intent in intent_list:
                        searched = search_string(vm_analysis, intent) or \
                            search_manifest_intent(intent, manifest_intents)
                        if searched:
                            unclaimed_permissions.remove(permission)
                            break
                    
                
                # Search contentprovider
                contentprovider_list = get_contentprovider_list(permission)
                if contentprovider_list:
                    for contentprovider in contentprovider_list:
                        searched = search_string(vm_analysis, contentprovider)
                        if searched:
                            unclaimed_permissions.remove(permission)
                            break
            except Exception,ex:
                log.exception(ex)
                continue
                
        return unclaimed_permissions

# Run
if __name__ == '__main__':
    import datetime 
    current_time = datetime.datetime.now().time()
    print current_time.isoformat()
    
    permission_scanner = PermissionScanner(r'E:\01-MobileSec\01-Android\TestApks\0AA58468ED13063DF55FD3C579C22431.apk')
    permission_scanner.start_analysis()
    print permission_scanner.get_certificate_info()
    print permission_scanner.get_unclaimed_permissions()
    
    current_time = datetime.datetime.now().time()
    print current_time.isoformat()
        
        
        
        
            
            
        
    
        
        
        
        




    