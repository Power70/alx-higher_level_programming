#!/usr/bin/python3

def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    roman_numerals = {
        "I": 1, "V": 5, "X": 10, "L": 50,
        "C": 100, "D": 500, "M": 1000
    }
    integer_val = 0
    i = -1

    while (i > -len(roman_string)):
        if (
                roman_numerals[roman_string[i]] >
                roman_numerals[roman_string[i - 1]]
        ):
            integer_val += roman_numerals[roman_string[i]]
            integer_val -= 2 * roman_numerals[roman_string[i - 1]]
        else:
            integer_val += roman_numerals[roman_string[i]]
        i = i - 1

    if (i == -len(roman_string)):
        integer_val += roman_numerals[roman_string[i]]

    return integer_val
