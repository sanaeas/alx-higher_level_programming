#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        squares = list(map(lambda x: x**2, arr))
        new_matrix.append(squares)
    return new_matrix
