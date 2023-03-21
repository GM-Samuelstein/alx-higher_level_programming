#!/usr/bin/python3

def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.

    Args:
        a_dictionary: The given dictionary.

    Returns:
        best_key: The key with the biggest integer value.
    """
    if a_dictionary:
        best_key = ""
        highscore = 0
        for key, value in a_dictionary.items():
            if value > highscore:
                highscore = value
                best_key = key
    else:
        return None

    return best_key
