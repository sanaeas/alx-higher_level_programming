#!/usr/bin/python3
"""Module defines the class LockedClass"""


class LockedClass:
    """prevents the user from dynamically creating new instance attributes"""
    __slots__ = ['first_name']
