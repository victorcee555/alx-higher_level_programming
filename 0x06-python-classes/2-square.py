#!/usr/bin/python3
"""This module demonstrates a class with
private instance attribute: size."""


class Square:
    """This is a class 'Square' that defines
    a square by:(based on 1-square.py)"""

    def __init__(self, size=0):
        """Thois is an instance with private
        instace attribute: size"""

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
