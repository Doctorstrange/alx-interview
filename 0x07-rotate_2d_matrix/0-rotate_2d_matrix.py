#!/usr/bin/python3
""" Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    for x, y in enumerate(zip(*reversed(matrix))):
        matrix[x] = list(y)


if __name__ == '__main__':
    the_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """ editing matrix in place """
    rotate_2d_matrix(the_matrix)
    print(the_matrix)
