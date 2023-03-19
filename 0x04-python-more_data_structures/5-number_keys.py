#!/usr/bin/python3

def number_keys(a_dictionary):
    """
    A function that returns the number of keys in a dictionary.

    Args:
        a_dictionary: The given dictionary.

    Returns:
        nb_keys: The number of keys in the given dictionary.
    """
    nb_keys = 0
    for key in a_dictionary:
        nb_keys += 1

    return nb_keys
