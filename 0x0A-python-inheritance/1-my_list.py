#!/usr/bin/python3
"""Module defines the class MyList"""


class MyList(list):
    """a subclass that inherits from list"""
    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
