#!/usr/bin/python3
"""Upgraded Student class Module"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes instances of the class with public instance
        attributes - `first_name`, `last_name` and `age`
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance
        Args:
            attrs (list): a list of strings, only attribute names contained
            in this list are retrieved. Otherwise, all attributes are retrieved
        """
        attr_dict = {}
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for attribute in attrs:
            if attribute in self.__dict__.keys():
                attr_dict[attribute] = (self.__dict__)[attribute]
        return attr_dict
