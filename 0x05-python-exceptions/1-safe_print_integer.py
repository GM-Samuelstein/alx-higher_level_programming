#!/usr/bin/python3

def safe_print_integer(value):
    """
    A function that prints an integer with `"{:d}".format()`.

    Args:
        value: The value to be printed.

    Returns:
        has_been_print: True, if value has been correctly printed.
            (It means the value is an integer). Otherwise, returns False
    """
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        return False
    else:
        return True
