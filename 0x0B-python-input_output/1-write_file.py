#!/usr/bin/python3
"""Module for write_file function"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF8)
    Args:
        filename (str): the name of the file to write into
        text (str): the context that will be written into the file
    Returns:
        the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        no_of_written_chars = f.write(text)

        return (no_of_written_chars)
