#!/usr/bin/python3
"""Define the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from the Base class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize attributes of the square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Access the size attribute of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value of the size attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of an instance"""
        if args:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """String representation of a Square instance"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
