#!/usr/bin/python3
"""Rectangle class module"""


class Rectangle:
    """Class from which rectangle objects can be instantiated"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle object.
        Gives the rectangle object a width of 0 and height of 0
        on instantiation.

        Args:
            width (int, optional): the width of the rectangle
            height (int, optional): the height of the rectangle
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """acts as a getter, retrieves the width of the rectangle object"""
        return self.__width

    @width.setter
    def width(self, value):
        """acts as a setter, sets the width of the rectangle to the
        given value
        Args:
            value (int): the new width of the rectangle object
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """acts as a getter, retrieves the height of the rectangle object"""
        return self.__height

    @height.setter
    def height(self, value):
        """acts as a setter, sets the height of the rectangle to the
        given value
        Args:
            value (int): the new height of the rectangle object
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
