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

    def area(self):
        """Calculate the area of the ractangle"""
        return self.width * self.height

    def display(self):
        """
        Print in stdout the Rectangle instance
        Using the character # and taking care of x and y
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """Update the attributes of an instance"""
        if args:
            try:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except IndexError:
                pass
        elif kwargs:
            for key, val in kwargs.items():
                setattr(self, key, val)

    def __str__(self):
        """String representation of a Rectangle instance"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"
