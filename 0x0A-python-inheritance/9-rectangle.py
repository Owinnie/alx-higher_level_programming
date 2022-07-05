#!/usr/bin/python3

"""Write a class Rectangle
that inherits BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle extends BaseGeometry"""
    def __init__(self, width, height):
        """Initialize"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self, width, height):
        """Find / return area"""
        return (self.__width * self.__height)

    def __str___(self):
        """Prints informal str"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
