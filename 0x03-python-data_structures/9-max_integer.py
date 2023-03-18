#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    A function that finds the biggest integer of a list.
    """
    if len(my_list) == 0:
        max_value = None
    else:
        max_value = my_list[0]
        for value in my_list:
            if value > max_value:
                max_value = value
            else:
                continue
    return max_value
