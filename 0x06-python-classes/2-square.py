#!/usr/bin/python3
"""This module shows a Square class hat defines a square by:
   - Private instance attribute
   - optional param (size)
"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializes the square object.

        Gives the square object a size on instantiation.
        If size is negative or is not an integer, an error is raised

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
