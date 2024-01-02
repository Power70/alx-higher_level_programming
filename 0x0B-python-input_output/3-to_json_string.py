#!/usr/bin/python3
"""Module for to_json_string function"""

import json


def to_json_string(my_obj):
    """Converts an object to its JSON representation
    Args:
        my_obj (obj): the object that needs to be serialized/converted
        to JSON
    Returns:
        the JSON representation of `my_obj`
    """
    return (json.dumps(my_obj))
