#!/usr/bin/python3
"""7-add_item module"""
import os
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if not os.path.exists(filename):
    with open(filename, 'w', encoding="utf-8") as f:
        obj = []
        json_data = json.dumps(obj)
        f.write(json_data)
data_list = list(load_from_json_file(filename))

for i in range(len(sys.argv)):
    if (i == 0):
        continue
    data_list.append(sys.argv[i])

save_to_json_file(data_list, filename)
