#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """Pascal's triangle function"""
    triangle = []
    if n > 0:
        for i in range(1, n + 1):
            row = []
            col = 1
            for j in range(1, i + 1):
                row.append(col)
                col = col * (i - j) // j
            triangle.append(row)
    return triangle
