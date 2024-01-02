#!/usr/bin/python3
"""Module for from_json_string function"""
import json


def from_json_string(my_str):
    """Converts JSON string to an object (Python data structure)
    Args:
        my_str: the JSON string/representation
    Returns:
        an object (Python datat structure) representated by JSON string
    """
    return (json.loads(my_str))
