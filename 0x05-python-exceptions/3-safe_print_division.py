#!/usr/bin/python3

def safe_print_division(a, b):
    """
    A function that divides 2 integers and prints the result.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        result: The value of the division, otherwise: None
    """
    try:
        result = a / b
    except ZeroDivisionError as ze:
        result = None
    finally:
        print("Inside result: {}".format(result))

    return result
