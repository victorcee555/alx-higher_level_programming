#!/usr/bin/python3

"""This module demonstates how to create a
private instance attribute of a class"""


class Square:
    """This is a class 'Square' that defines
    a square by :(based on 0-square.py)"""

    def __init__(self, size):
        """A method with private instance attribute: size"""

        self.__size = size
