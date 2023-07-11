#!/usr/bin/python3
"""Module defines pascal_triangle function"""


def pascal_triangle(n):
    """
    returns a list of lists of integers
    representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        sub = []
        for j in range(i + 1):
            if j == 0 or j == i:
                sub.append(1)
            else:
                sub.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
        triangle.append(sub)
    return triangle
