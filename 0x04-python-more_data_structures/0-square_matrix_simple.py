#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    A function that computes the square value of all integers of a matrix.
    """
    copy_matrix = matrix.copy()
    new_matrix = []
    for row in copy_matrix:
        temp_list = []
        for column in row:
            temp_list.append(column ** 2)
        new_matrix.append(temp_list)
    
    return new_matrix
