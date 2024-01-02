#!/usr/bin/python3
"""Module for append_write function"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text fle (UTF8)

    Args:
        filename (str): name of file that will be updated by adding new text
        text (str): the contents to add to `filename`
    Returns:
        the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        no_of_appended_chars = f.write(text)

        return (no_of_appended_chars)
