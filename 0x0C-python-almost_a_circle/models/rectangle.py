#!/usr/bin/python3
"""Define the Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class that inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize attributes of the rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Access the width attribute of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Access the height attribute of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """Access the x attribute of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the value of the x attribute"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """Access the y attribute of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the value of the y attribute"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value
