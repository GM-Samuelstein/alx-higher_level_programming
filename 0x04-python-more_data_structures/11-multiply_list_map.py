#!/usr/bin/python3

def multiply_list_map(my_list=[], number=0):
    """
    A function that returns a list with all values multiplied by a number
    without using any loops.

    Args:
        my_list: The initial list.
        number: The number with which each number in the list will be
            multiplied.

    Returns:
        new_list: A new list with the same length as the initial list,
            where each value has been multiplied by `number`.
    """
    new_list = list(map(lambda list_item: list_item * number, my_list))
    return new_list
