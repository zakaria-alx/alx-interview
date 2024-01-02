#!/usr/bin/env
"""
Create a function def pascal_triangle(n): that returns a list of lists of 
integers representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
You can assume n will be always an integer

Expected Output:
[1]
[1,1]
[1,2,1]
[1,3,3,1]
[1,4,6,4,1]
"""

def pascal_triangle(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
