#!/usr/bin/python3
"""Module that says the person's name"""


def say_my_name(first_name, last_name=""):
    """
    Prints a person's name by combining the first name and last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
