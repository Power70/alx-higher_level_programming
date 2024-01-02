#!/usr/bin/python3
"""Module for class_to_json function"""


def class_to_json(obj):
    """Function that converts an object into a representation
    that can be serialized
    Args:
        obj (object): an instance of a class that will be converted and
        in which all of its attributes are serializable
    Returns:
        The dictionary description with simple data structure for JSON
        serialization of the object
    """
    # return (obj.__dict__) OR
    return (vars(obj))
