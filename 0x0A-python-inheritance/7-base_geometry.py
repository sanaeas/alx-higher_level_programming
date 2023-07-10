#!/usr/bin/python3
"""Module defines BaseGeometry class"""


class BaseGeometry():
    """A base geometry class"""
    def area(self):
        """A method that raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A method that validates value"""
        if type(value) != int and type(value) != float:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
