#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0 or all(not row for row in matrix):
        print()
        return matrix

    for i in range(3):
        for j in range(3):
            if j == 2:
                print("{:d}".format(matrix[i][j]), end="")
            else:
                print("{:d}".format(matrix[i][j]), end=" ")
        print()
