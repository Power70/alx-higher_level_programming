#!/usr/bin/python3
"""Square class module"""


class Square:
    """Class from which square objects can be instantiated"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square object with size and position
        Args:
            size (int, optional): The size of the square object
            position (:obj: 'tuple', optional): the position of the object
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """size getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter
        Args:
            value (int): the new size of the square object
        Raises:
            TypeError: if the  value is not an integer
            ValueError: if the value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter
        Args:
            value (tuple): the new position of the square consisting
            of two positive integers
        Raises:
            TypeError: if either or both of the tuple elements
            are not positive integers
        """
        if (type(value) is not tuple) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for row in range(0, self.size):
                for space in range(self.position[0]):
                    print(" ", end="")
                for column in range(self.size):
                    print("#", end="")
                print()
