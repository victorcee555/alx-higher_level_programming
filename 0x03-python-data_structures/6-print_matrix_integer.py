#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or all(not row for row in matrix):
        print()
        return matrix
    row = len(matrix)
    column = len(matrix[0])
    for i in range(row):
        for j in range(column):
            if j == 2:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
        print()
