#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    second_matrix = []
    for i in matrix:
        second_matrix.append(list(map(lambda x:x**2, i)))

    return second_matrix
