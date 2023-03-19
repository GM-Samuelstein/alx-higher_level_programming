#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    A function that replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: The given dictionary,
        key: The key to be created or updated.
        value: The new value for the key.

    Returns:
        a_dictionary: An updated version of the given dictionary.
    """
    a_dictionary[key] = value

    return a_dictionary
