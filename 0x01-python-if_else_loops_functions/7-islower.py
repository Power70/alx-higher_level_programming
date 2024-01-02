#!/usr/bin/python3
def islower(c):
    unicode_val = ord(c)
    if unicode_val in range(97, 124):
        return True
    else:
        return False
