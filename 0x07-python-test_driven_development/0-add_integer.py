#!/usr/bin/python3
"""Module provides addition operations"""


def add_integer(a, b=98):
    """
    Calculates the sum of two numbers
    Returns the sum of a and b as an integer
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
