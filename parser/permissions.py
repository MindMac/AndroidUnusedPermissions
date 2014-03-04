#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2014-3-3

@author: Wenjun Hu
'''

from permissions_map.api import API_PERMISSION_MAP
from permissions_map.intent import INTENT_PERMISSION_MAP
from permissions_map.contentprovider import CONTENTPROVIDER_PERMISSION_MAP
# Generate Permission list

dst_file = r'../permissions_map/permissions.py'

dst_file_obj = open(dst_file, 'w')

dst_file_obj.write('#!/usr/bin/env python\n')
dst_file_obj.write('#-*- coding: utf-8 -*-\n\n')
dst_file_obj.write('#Permission List\n\n')

dst_file_obj.write('PERMISSIONS = [\n')

permission_list = []

permission_list.extend(API_PERMISSION_MAP.keys())
permission_list.extend(INTENT_PERMISSION_MAP.keys())
permission_list.extend(CONTENTPROVIDER_PERMISSION_MAP.keys())

permission_list = list(set(permission_list))
print permission_list

for permission in permission_list:
    dst_file_obj.write("\t'%s', \n" % permission)

dst_file_obj.write(']')
dst_file_obj.close()

