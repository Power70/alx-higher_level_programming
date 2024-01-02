#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # my_list = [[replace for search in row] for row in my_list]
    new_list = my_list.copy()
    for x in new_list:
        if x == search:
            new_list[new_list.index(x)] = replace
    return new_list
