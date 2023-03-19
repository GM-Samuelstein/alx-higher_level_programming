#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    A function that returns a set of common elements in two sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        c_set: A set containing the common elements in the two given sets.
    """
    c_set = set_1 & set_2

    return c_set
