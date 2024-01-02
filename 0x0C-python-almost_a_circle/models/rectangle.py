#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes instances of Rectangle class with given attributes
        Args:
            width (int): the width of the rectangle (Private instance attr)
            height (int): the height of the rectangle (Private instance attr)
            x (int, optional): the x-coordinate of the rectangle object
            y (int, optional): the y-coordinate of the rectangle object
            id (int): id (unique identifier) of the rectangle object
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter, gets the width of the rectangle object"""
        return self.__width

    @width.setter
    def width(self, value):
        """Wdith setter, sets the width of the rectangle object to the given
        value
        Args:
            value (int): the new width of the rectangle object
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter, sets the height of the rectangle object to the
        given value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle object
        Returns:
            the area of the rectangle object
        """
        return (self.width * self.height)

    def display(self):
        """Prints in stdout the Rectangle instance with character #"""
        for vert_space in range(self.y):
            print()

        for i in range(self.height):
            for horizon_space in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        or assignes a key/value argument to attributes

        Args:
            args (list/tuple): for any number of positional arguments
            kwargs (dict): for any number of keyword arguments
        """
        if args is not None and len(args) > 0:
            for index, arg in enumerate(args):
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.height = arg
                elif index == 3:
                    self.x = arg
                elif index == 4:
                    self.y = arg

        else:
            if kwargs is not None and len(kwargs) > 0:
                for key, value in kwargs.items():
                    if key == "id":
                        self.id = value
                    elif key == "width":
                        self.width = value
                    elif key == "height":
                        self.height = value
                    elif key == "x":
                        self.x = value
                    elif key == "y":
                        self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a rectangle object"""
        attr_list = ["id", "width", "height", "x", "y"]

        return {attr: getattr(self, attr) for attr in attr_list}

    def __str__(self):
        """Defines the string representation of the Rectangle object"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height
                )
