#!/usr/bin/python3
"""This module demonstrates the definition of a square
with Private instance attribute (size), optional parameter (size)
and public instance method
"""


class Square:
    """The class from which square objects can be instantiated"""
    def __init__(self, size=0):
        """On instantiation, gives the square object an initial size

        Args:
            size (int, optional): The size of the square object
        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculates the area of a square object

        Returns:
            the calculated square area
        """
        return (self.__size)**2
