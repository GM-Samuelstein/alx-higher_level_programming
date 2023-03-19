#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    A function that prints a dictionary by ordered keys.

    Args:
        a_dictionary: The given dictionary.

    Returns:
        No return value.
    """
    sorted_dictionary = sorted(list(a_dictionary))
    for key in sorted_dictionary:
        print(f"{key}: {a_dictionary[key]}")
