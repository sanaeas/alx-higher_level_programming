#!/usr/bin/python3
"""Module defines is_same_class function"""


def is_same_class(obj, a_class):
    """returns True if the object is an instance of the specified class"""
    return type(obj) == a_class
