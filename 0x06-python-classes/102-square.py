#!/usr/bin/python3
"""Defining class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def __eql__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __negt__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lst__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __lseq__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __grt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __greq__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
