#!/usr/bin/python3
"""Module defines inherits_from function"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherited
    from the specified class
    """
    return issubclass(obj.__class__, a_class) and type(obj) != a_class
