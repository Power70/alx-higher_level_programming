#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    different_elements = []

    for i in set_1:
        if i not in set_2:
            different_elements.append(i)

    for i in set_2:
        if (i not in set_1) and (i not in different_elements):
            different_elements.append(i)

    return different_elements
