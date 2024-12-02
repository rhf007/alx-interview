#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    perimeter = 0
    length = len(grid)
    row = len(grid[0])

    for i in range(length):
        for j in range(row):
            if grid[i][j] == 1:
                for k, z in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    f, g = i + k, j + z
                    if f >= length or g >= row or f < 0 or g < 0 or grid[f][g] == 0:
                        perimeter += 1
    return perimeter
