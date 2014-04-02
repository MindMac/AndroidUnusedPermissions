#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2014-4-2

@author: Wenjun Hu
'''

def get_cpu_count():
    import multiprocessing
    return multiprocessing.cpu_count()

def search_method(vm_analysis, class_name, method_name):
    searched_method_list = vm_analysis.tainted_packages.search_methods(class_name, method_name, ".")
    if searched_method_list:
        return True
    else:
        return False
    
def search_string(vm_analysis, string_name):
    for s, _ in vm_analysis.tainted_variables.get_strings() :
        string_info = s.get_info()
        if string_name in string_info :
            return True
    return False

def get_manifest_intents(apk):
    return apk.get_elements('action', 'android:name')

def search_manifest_intent(intent, intents):
    return intent in intents
    
    
