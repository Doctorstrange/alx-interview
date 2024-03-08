#!/usr/bin/python3
"""list of lists of integers representing the Pascal’s triangle"""


def pascal_triangle(n):
    """list of lists of integers representing the Pascal’s triangle"""

  if n <= 0:
    return []

  triangle = [[1]]  # Initialize with first row (1)

  for i in range(1, n):
    # Build the next row based on the previous row
    row = [1]  # Start with 1 at the beginning
    for j in range(1, i):
      # Get the sum of elements above us in the previous row
      row.append(triangle[i-1][j-1] + triangle[i-1][j])
    row.append(1)  # End with 1
    triangle.append(row)

  return triangle
