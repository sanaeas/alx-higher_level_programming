#!/usr/bin/python3
"""Module provides a matrix divider"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number
    Returns a new matrix
    """
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or \
            any(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    mat_len = len(matrix)
    for i in range(mat_len - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for i in matrix:
        new_row = []
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
            else:
                new_row.append(round(j / div, 2))
        new_matrix.append(new_row)

    return new_matrix
