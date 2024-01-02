#!/usr/bin/python3
"""Module for load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Function that creates an object from a JSON file
    Args:
        filename (str): the name of the JSON file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
