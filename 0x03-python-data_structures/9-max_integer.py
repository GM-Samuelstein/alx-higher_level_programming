#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    A function that finds the biggest integer of a list.
    """
    max_value = 0

    if len(my_list) == 0:
        max_value = None
    else:
        for value in my_list:
            if value > max_value:
                max_value = value
            else:
                continue
    return max_value
