#!/usr/bin/python3
"""Module that demonstrates the concept of Pascal's triangle"""


def pascal_triangle(n):
    """Returns a list of integers representing the Pascal's triangle
    of n"""
    triangle_list = []

    if n <= 0:
        return (triangle_list)

    new_list = []
    new_list_2 = []
    for i in range(1, n + 1):
        if i == 1:
            new_list.insert(0, 1)
            triangle_list.append(new_list)
            continue
        for j in range(i):
            if j == 0 or j == i - 1:
                new_list_2.insert(j, 1)
            else:
                new_list_2.insert(j, new_list[j] + new_list[j - 1])
        new_list = new_list_2[:]
        new_list_2.clear()
        triangle_list.append(new_list)

    return triangle_list
