#!/usr/bin/python3
"""Module that prints a square"""


def print_square(size):
    """
    Prints a square with the character #
    Returns nothing
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for _ in range(size):
            for _ in range(size):
                print("#", end="")
            print("")
