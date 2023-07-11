#!/usr/bin/python3
"""Module defines write_file function"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file
    returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
