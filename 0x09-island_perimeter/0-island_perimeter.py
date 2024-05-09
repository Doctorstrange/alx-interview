#!/usr/bin/python3
"""returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid
    Returns:
        0 represents water
        1 represents land
    """
    breath = len(grid[0])
    length = len(grid)
    corner = 0
    size = 0

    for x in range(length):
        for j in range(breath):
            if grid[x][j] == 1:
                size += 1
                if (j > 0 and grid[x][j - 1] == 1):
                    corner += 1
                if (x > 0 and grid[x - 1][j] == 1):
                    corner += 1
    return size * 4 - corner * 2
