#!/usr/bin/python3

"""Defining class Square"""


class Square:
    """Adding unto the initialization"""

    def __init__(self, size=0):
        """Run when new instance of class
        is created.
        Args:
            size (int): The size of the new square.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set size"""
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.__size * self.__size)