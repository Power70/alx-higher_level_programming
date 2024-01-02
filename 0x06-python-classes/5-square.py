#!/usr/bin/python3
"""Square class module"""


class Square:
    """Class from which square objects can be instantiated/created"""
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

    @property
    def size(self):
        """works as a getter, retrieves the size of the square object
        Returns:
            the size of the square object
        """
        return self.__size

    @size.setter
    def size(self, value):
        """works as a setter, reset the size of the square object to
        the given value
        Args:
            value (int): the new size of the square object
        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Method that returns the current square area
        Returns:
            the square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square with the character #"""
        for height in range(self.__size):
            for width in range(self.__size):
                print("#", end="")
            print()

        if self.__size == 0:
            print()
