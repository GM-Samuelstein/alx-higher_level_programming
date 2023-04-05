#!/usr/bin/python3
"""
A program that solves the N queens puzzle.

The N queens puzzle is the challenge of placing N chess queens on an N x N
chessboard such that no two queen attack each other on the board.This means
that no two queens can share the same row, column, or diagonal on the
chessboard.
"""
import sys


class NQueens:
    """

    """

    def __init__(self, N):
        """
        Initializes a new puzzle-set object with the given attribute.

        Args:
            N (int) :
                The size of the chess board.

        """
        self.board = N
        self.solutions = []

    def solve_puzzle():
        pass

    def get_solutions():
        pass


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    else:
        print("Cheers! The program ran successfully.")
