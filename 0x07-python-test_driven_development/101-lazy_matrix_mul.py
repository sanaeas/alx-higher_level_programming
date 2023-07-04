#!/usr/bin/python3
"""Module uses the module NumPy to multiply 2 matrices"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices by using the module NumPy"""
    return np.matmul(m_a, m_b)
