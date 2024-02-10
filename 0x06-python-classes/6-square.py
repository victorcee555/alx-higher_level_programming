#!/usr/bin/python3
"""This module demonstrates a class with
private instance attribute: size."""


class Square:
    """This is a class 'Square' that defines
    a square by:(based on 4-square.py)"""

    def __init__(self, size=0, position=(0, 0)):
        """This is an instance with private
        instace attribute: size"""

        self.__size = size
        self.__position = position

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    @property
    def size(self):
        """This is a property instance that
        retreives the value of self"""

        return self.__size

    @size.setter
    def size(self, value):
        """This is a property setter instance that
        sets the value for the private instance: size"""

        self.__size = value

        if type(self.__size) is not int:
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """This is an instance that returns
        the current square area"""

        return self.__size ** 2

    def my_print(self):
        """This is an instance that prints to the
        stdout the square with the character #."""

        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(' ' * self.__position[0], end="")
                print("#" * self.__size)

    @property
    def position(self):
        """This is an instance that returns the value
        of the private attribute: position."""

        return self.__position

    @position.setter
    def position(self, value):
        """This is a property setter instance that
        sets the value of the private instance: position."""

        self.__position = value

        if type(self.__size) is not tuple and len(self.__position) == 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if self.__position[0] or self.__position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
