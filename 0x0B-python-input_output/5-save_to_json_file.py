#!/usr/bin/python3
"""Module for save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """Function that writes an object to a text file, using a JSON
    represention

    Args:
        my_obj (obj): the object that will be serialized
        filename: the name of the JSON file
    """
    with open(filename, 'w', encoding="utf-8") as f:
        json_data = json.dumps(my_obj)
        f.write(json_data)
