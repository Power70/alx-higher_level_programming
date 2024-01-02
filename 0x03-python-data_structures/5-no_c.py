#!/usr/bin/env python3
def no_c(my_string):
    new_str = ""

    for j in my_string:
        if j not in ["C", "c"]:
            new_str += j
    return new_str
