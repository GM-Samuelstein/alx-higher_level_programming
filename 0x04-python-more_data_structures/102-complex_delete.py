#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    A function that deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary: The given dictionary.

    Returns:

    """
    death_row = []
    for dict_key, dict_value in a_dictionary.items():
        if dict_value == value:
            death_row.append(dict_key)
        else:
            continue

    for inmate in death_row:
        del a_dictionary[inmate]

    return a_dictionary
