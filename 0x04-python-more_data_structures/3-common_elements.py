#!/usr/bin/python3

def common_elements(set1, set2):
    common_elements = []

    for i in set1:
        if (i in set1) and (i in set2):
            common_elements.append(i)

    return common_elements
