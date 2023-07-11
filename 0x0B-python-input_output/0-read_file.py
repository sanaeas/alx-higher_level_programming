#!/usr/bin/python3
"""Module defines read_file function"""


def read_file(filename=""):
    """a function that reads a text file and prints it"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
