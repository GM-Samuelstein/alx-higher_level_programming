#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    A function that computes the square value of all integers of a matrix
    using `map`.

    Args:
        matrix: The given matrix, a 2 dimensional array.

    Returns:
        new_matrix: A new matrix of the same size as the input matrix,
        and each value is the square of the value of the input.
    """
    new_matrix = matrix.copy()
    # x = matrix row
    # y = matrix column

    new_matrix = \
        list(map(lambda x: list(map(lambda y: y ** 2, x)), new_matrix))

    return new_matrix
