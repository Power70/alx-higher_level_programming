#!/usr/bin/python3
"""Rectangle class module"""


class Rectangle:
    """Class that defines a rectangle"""
    def __init__(self, width=0, height=0):
        """On instantiation, gives the rectangle width and height
        Args:
            width (int, optional): the width of the rectangle object
            height (int, optional): the height
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter
        Args:
            value (int): the new width of the rectangle
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
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter
        Args:
            value (int): the new height of the rectangle object
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if (self.width == 0) or (self.height == 0):
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """Method that creates a new string object from the given object"""
        string = ""

        if (self.width == 0) or (self.height == 0):
            return string
        for i in range(self.height):
            for j in range(self.width):
                print(string + "#", end="")
            if i < self.height - 1:
                print()
        return string

    def __repr__(self):
        """Method that returns a sting representation of the rectangle
        to be able to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)
