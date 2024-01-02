#!/usr/bin/python3
"""This module provides a Square class. Instances of the class
are initialized with a size, which is 0 by default.
Property is also used as getter and setter for the square
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

    @property
    def size(self):
        """works as a getter, retrieves the size of the square
        Returns:
            the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """works as a setter, reset the size of the square to the
        given value
        Args:
            value(int): the new square object size
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
