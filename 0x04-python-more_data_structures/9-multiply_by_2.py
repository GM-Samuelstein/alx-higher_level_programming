#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary: The given dictionary.

    Returns:
        new_dict: A new dictionary with all values multiplied by 2.
    """
    new_dict = a_dictionary.copy()
    for key in new_dict:
        new_dict[key] *= 2
    return new_dict
