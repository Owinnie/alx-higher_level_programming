#!/usr/bin/python3

"""Defining class Square"""


class Square:
    """Square implementation
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    @property
    def position(self):
        """Get/set the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """calculates the square area
        """
        return (self.__size ** 2)

    def my_print(self):
        """prints a square  with the corresponding size
        """
        if (self.__size == 0):
            print('')

        for i in range(self.__size):
            print('#' * self.__size)
        i = 0
