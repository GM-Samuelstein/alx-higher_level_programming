#!/usr/bin/python3

def no_c(my_string):
    """
    A function that removes all characters `c` and `C` from a string.
    """
    new_string = ""
    for char in my_string:
        if char == "c" or char == "C":
            continue
        else:
            new_string = new_string + char
    return new_string
