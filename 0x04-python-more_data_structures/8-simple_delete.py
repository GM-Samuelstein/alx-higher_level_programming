#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    A function that deletes a key in a dictionary.

    Args:
        a_dictonary: The given dictionary.
        key: The key to be deleted, if it exists.

    Returns:
        a_dictionary: The given dictionary without the key (if it existed),
            or same dictionary, if the key does not exist.
    """
    if a_dictionary.get(key):
        del a_dictionary[key]
    
    return a_dictionary
