#!/usr/bin/python3
"""Module defines append_write function"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file
    returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
