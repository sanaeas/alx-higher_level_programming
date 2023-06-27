#!/usr/bin/python3
"""A module that defines a node of a singly linked list"""


class Node:
    """A node a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        current = self.__head
        if (current is None) or \
                (current.data > new_node.data):
            self.__head = new_node
            new_node.next_node = current
        else:
            while (current is not None) and \
                    (current.next_node is not None):
                if current.next_node.data > new_node.data:
                    break
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data)
            current = current.next_node
            if current is not None:
                result += "\n"
        return result
