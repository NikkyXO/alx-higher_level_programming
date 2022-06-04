#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    A function that prints a matrix of integers
    """

    if len(matrix[0]) != 0:
        rows = len(matrix)
        column = len(matrix[0])

        for i in range(rows):
            for j in range(column):
                if j == column - 1:
                    print("{:d}".format(matrix[i][j]))
                else:
                    print("{:d} ".format(matrix[i][j]), end="")

    else:
        print()
