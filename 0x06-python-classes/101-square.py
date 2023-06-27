#!/usr/bin/python3
"""Module creating a Square class"""


class Square:
    """Define a Square class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple) or (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) != int or \
                type(value[1]) != int or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size**2

    def __str__(self):
        if self.__size == 0:
            return ""
        square_lines = []
        for _ in range(self.__position[1]):
            square_lines.append("\n")
        for _ in range(self.__size):
            square_lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(square_lines)
