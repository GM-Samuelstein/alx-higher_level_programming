#!/usr/bin/python3

def weight_average(my_list=[]):
    """
    A function that returns the weighted average of all integers tuple.
    tuple = (<score>, <weight>)

    Args:
        my_list: A list of tuples. Each tuple is a pair of `score` and
            `weight`.

    Returns:
        result: The average of all the tuples.
    """
    if not my_list:
        return 0

    numerator = 0
    denominator = 0

    for tuple in my_list:
        score = tuple[0]
        weight = tuple[1]
        numerator += score * weight
        denominator += weight

    result = numerator / denominator

    return result
