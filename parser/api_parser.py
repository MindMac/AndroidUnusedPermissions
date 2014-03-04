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
permission_count = 0

while src_line:
    if src_line.startswith('Permission'):
        permission_count += 1
        if permission_count > 1:
            dst_file_obj.write('\t],\n')
        permission = src_line.split(':')[-1]
        permission = permission.strip()
        dst_file_obj.write("\t'%s':[\n" % (permission))
    elif src_line.startswith('<'):
        res = api_pattern.findall(src_line)
        if res:
            class_name = res[0][0]
            class_name = class_name.replace('.', '/')
            class_name = 'L%s' % class_name
            method_name = res[0][1]
            dst_file_obj.write("\t\t('%s', '%s'), \n" %(class_name, method_name))
            
    src_line = src_file_obj.readline()

dst_file_obj.write('\t],\n')
dst_file_obj.write('}')
src_file_obj.close()  
dst_file_obj.close()

        
        
    
        
    


