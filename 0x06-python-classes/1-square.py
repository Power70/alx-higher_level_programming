#!/usr/bin/python3
"""This module demonstrates the definition of a square
with private instance atribute - size
"""


class Square:
    """The class from which square objects can be instantiated """
    def __init__(self, size):
        """The __init__ method of the Square class.
        Gives the initial size of the new square object.

        Args:
            size (int): The size of the square instance once created.
            A private instance attribute
        """
        self.__size = size
