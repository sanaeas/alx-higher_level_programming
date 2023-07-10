#!/usr/bin/python3
"""Module defines add_attribute function"""


def add_attribute(obj, name, value):
    """adds a new attribute if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
