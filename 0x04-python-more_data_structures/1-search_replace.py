#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences of an element by another in a
    new list.

    Args:
        my_list: The initial list.
        search: The element to replace in the list.
        replace: The new element.

    Returns:
        new_list: A new list that refelects the replacement(s).
    """
    new_list = my_list.copy()
    for element in range(len(new_list)):
        if new_list[element] == search:
            new_list[element] = replace
        else:
            continue
    return new_list
