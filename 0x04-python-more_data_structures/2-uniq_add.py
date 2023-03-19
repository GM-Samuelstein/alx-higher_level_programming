#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    A function that adds all unique integers in a list.
    (only once for each integer).

    Args:
        my_list: The initial list.

    Returns:
        sum: The sum of all unique integers in the input list.
    """
    uniq = set(my_list)
    sum = 0
    for integer in uniq:
        sum += integer
    return sum
