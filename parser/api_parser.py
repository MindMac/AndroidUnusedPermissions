#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2014-3-2

@author: Wenjun Hu
'''

import re

# Parse API Permission map from PScount to generate Python dictionary

src_file = r'../permissions/api.txt'
dst_file = r'../permissions_map/api.py'
api_pattern = re.compile(r'\<(.+):\s+.+\s+(\w+)')

src_file_obj = open(src_file, 'r')
dst_file_obj = open(dst_file, 'w')

dst_file_obj.write('#!/usr/bin/env python\n')
dst_file_obj.write('#-*- coding: utf-8 -*-\n\n')
dst_file_obj.write('#API Permission Map\n\n')

dst_file_obj.write('API_PERMISSION_MAP = {\n')

src_line = src_file_obj.readline()

permission_api_map = {}

while src_line:
    if src_line.startswith('Permission'):

        permission = src_line.split(':')[-1]
        permission = permission.strip()
        permission_api_map[permission] = []
    elif src_line.startswith('<'):
        res = api_pattern.findall(src_line)
        if res:
            class_name = res[0][0]
            class_name = class_name.replace('.', '/')
            class_name = 'L%s' % class_name
            method_name = res[0][1]
            permission_api_map[permission].append((class_name, method_name))
            
    src_line = src_file_obj.readline()

for permission, api_tuple_list in permission_api_map.items():
    api_tuple_list = list(set(api_tuple_list))

    for api_tuple in api_tuple_list:
        dst_file_obj.write("\t('%s;', '%s') : '%s' ,\n" % (api_tuple[0], api_tuple[1], permission))
        
dst_file_obj.write('}')
src_file_obj.close()  
dst_file_obj.close()

        
        
    
        
    


