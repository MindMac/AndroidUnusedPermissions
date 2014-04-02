#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2014-3-2

@author: Wenjun Hu
'''

# Parse API Permission map from PScount to generate Python dictionary

src_file = r'../permissions/contentprovider.txt'
dst_file = r'../permissions_map/contentprovider.py'

src_file_obj = open(src_file, 'r')
dst_file_obj = open(dst_file, 'w')

dst_file_obj.write('#!/usr/bin/env python\n')
dst_file_obj.write('#-*- coding: utf-8 -*-\n\n')
dst_file_obj.write('#ContentProvider Permission Map\n\n')

src_line = src_file_obj.readline()

contentprovider_permission_map = {}

while src_line:
    data_list = src_line.split()
    contentprovider = data_list[0].strip()
    permission = data_list[2].strip()
    if contentprovider_permission_map.has_key(permission):
        contentprovider_permission_map[permission].append(contentprovider)
    else:
        contentprovider_permission_map[permission] = []
        contentprovider_permission_map[permission].append(contentprovider)
            
    src_line = src_file_obj.readline()

src_file_obj.close()  

dst_file_obj.write('CONTENTPROVIDER_PERMISSION_MAP = {\n')

for permission, contentproviders in contentprovider_permission_map.items():
    contentproviders = list(set(contentproviders))
    if permission != 'pathPrefix' and permission != 'pathPattern':
        for contentprovider in contentproviders:
            dst_file_obj.write("\t'%s' : '%s', \n" % (contentprovider, permission))
        
dst_file_obj.write('}')
dst_file_obj.close()

        
        
    
        
    


