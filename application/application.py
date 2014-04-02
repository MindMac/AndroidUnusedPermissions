#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2014-3-2

@author: Wenjun Hu
'''

# Global imports
import logging

# PermissionScanner imports
from permissions_map.api import API_PERMISSION_MAP
from permissions_map.intent import INTENT_PERMISSION_MAP
from permissions_map.contentprovider import CONTENTPROVIDER_PERMISSION_MAP

# Logguer
log = logging.getLogger('log')


# Get api etc. by permission
def get_permission_by_api(api_tuple):
    return API_PERMISSION_MAP.get(api_tuple)

def get_permission_by_intent(intent):
    return INTENT_PERMISSION_MAP.get(intent)

def get_permission_by_contentprovider(contentprovider):
    return CONTENTPROVIDER_PERMISSION_MAP.get(contentprovider)

