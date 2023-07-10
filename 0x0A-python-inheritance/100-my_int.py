#!/usr/bin/python3
"""Module defines a class MyInt"""


class MyInt(int):
    """MyInt is a rebel of int class"""
    def __eq__(self, other):
        return not (self.real == other.real)

    def __ne__(self, other):
        return not (self.real != other.real)
