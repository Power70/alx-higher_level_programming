#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    b = my_list.copy()
    if (idx < 0):
        return my_list
    if (idx > len(my_list) - 1):
        return my_list
    else:
        b[idx] = element
        return b
