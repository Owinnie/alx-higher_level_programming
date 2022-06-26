#!/usr/bin/python

"""
Module 100-matrix_mul contains function
matrix_mul() that multiplies two matrices
"""


def matrix_mul(m_a, m_b):
    """ Multiply 2 matrices
    Args:
        m_a (list): matrix 1
        m_b (list): matrix 2
    Returns: new matrix--> row=m_a, col=m_b
    """
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    elif type(m_b) != list:
        raise TypeError("m_b must be a list")
    for rw in m_a:
        if type(rw) != list:
            raise TypeError("m_a must be a list of lists")
    for rw2 in m_b:
        if type(rw2) != list:
            raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    elif m_b == [] or m_b = [[]]:
        raise ValueError("m_b can't be empty")
    for rw in m_a:
        for el in rw:
            if type(el) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    for rw2 in m_b:
        for el2 in rw2:
            if type(el2) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    if not all(len(rw) == len(m_a[0]) for rw in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(rw2) == len(m_b[0]) for rw2 in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    pd_mat = []
    new_matrix = []
    
    for r in range(len(m_b[0])):
        new_rw = []
        for c in range(len(m_b)):
            new_rw.append(m_b[c][r])
        pd_mat.append(new_rw)

    for rw in m_a:
        new_rw = []
        for col in pd_mat:
            pd = 0
            for i in range(len(pd_mat[0])):
                pd += rw[i] * col[i]
            new_rw.append(pd)
        new_matrix.append(new_rw)

    return new_matrix
