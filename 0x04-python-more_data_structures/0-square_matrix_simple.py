#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    A function that computes the square value of all integers of a matrix.
    """
    new_matrix = []
    for row in matrix:
        temp_list = []
        for column in row:
            temp_list.append(column ** 2)
        new_matrix.append(temp_list)

    return new_matrix
