#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2014-3-2

@author: Wenjun Hu
'''

# Parse API Permission map from PScount to generate Python dictionary

src_file = r'../permissions/intent.txt'
dst_file = r'../permissions_map/intent.py'

src_file_obj = open(src_file, 'r')
dst_file_obj = open(dst_file, 'w')

dst_file_obj.write('#!/usr/bin/env python\n')
dst_file_obj.write('#-*- coding: utf-8 -*-\n\n')
dst_file_obj.write('#Intent Permission Map\n\n')

src_line = src_file_obj.readline()

intent_permission_map = {}

while src_line:
    data_list = src_line.split()
    intent = data_list[0].strip()
    permission = data_list[1].strip()
    if intent_permission_map.has_key(permission):
        intent_permission_map[permission].append(intent)
    else:
        intent_permission_map[permission] = []
        intent_permission_map[permission].append(intent)
            
    src_line = src_file_obj.readline()

src_file_obj.close()  

dst_file_obj.write('INTENT_PERMISSION_MAP = {\n')

for permission, intents in intent_permission_map.items():
    intents = list(set(intents))
    for intent in intents:
        dst_file_obj.write("\t'%s' : '%s', \n" % (intent, permission))
        
dst_file_obj.write('}')
dst_file_obj.close()

        
        
    
        
    


