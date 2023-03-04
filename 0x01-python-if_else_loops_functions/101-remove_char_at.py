#!/usr/bin/python3

def remove_char_at(str, n):
    """
    A python function that creates a copy of the string, removing the
    character at the position 'n'.
    """
    nstring = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            nstring = nstring + str[i]
    return nstring
