#!/usr/bin/python3
"""Rectangle class module"""


class Rectangle:
    """Class that defines a rectangle
    Attributes:
        number_of_instances (int): Number of available instances;
        a public class attr.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """On instantiation, gives the rectangle width and height
        Args:
            width (int, optional): the width of the rectangle object
            height (int, optional): the height
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
                print(string + str(self.print_symbol), end="")
            if i < self.height - 1:
                print()
        return string

    def __repr__(self):
        """Method that returns a sting representation of the rectangle
        to be able to recreate a new instance"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """Method that handles deletion of instances"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Method that returns the biggest rectangle object based
        on the area
        Args:
            rect_1 ('obj': Rectangle): first rectangle object
            rect_2 ('obj': Rectangle): another rectangle object
        Raises:
            TypeError: if any of the object is not an instance of
            Rectangle class
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
