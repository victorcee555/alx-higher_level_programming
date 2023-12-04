#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) or all(row for row in matrix):
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            for j in range(column):
                if j == column - 1:
                    print("{:d}".format(matrix[i][j]), end="")
                else:
                    print("{:d}".format(matrix[i][j]), end=" ")
            print()
    else:
        print()
                
