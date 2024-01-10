#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key, val in list(a_dictionary.items()):
        if val == value:
            del a_dictionary[key]

# Example usage:
my_dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 2, 'e': 1}
value_to_delete = 2

complex_delete(my_dictionary, value_to_delete)
print(my_dictionary)

