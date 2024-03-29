#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    A function that adds 2 tuples.
    """
    if len(tuple_a) == 0:
        a = 0
        b = 0
    elif len(tuple_a) == 1:
        a = tuple_a[0]
        b = 0
    else:
        a = tuple_a[0]
        b = tuple_a[1]

    if len(tuple_b) == 0:
        x = 0
        y = 0
    elif len(tuple_b) == 1:
        x = tuple_b[0]
        y = 0
    else:
        x = tuple_b[0]
        y = tuple_b[1]

    new_tuple = (a + x, b + y)
    return new_tuple
