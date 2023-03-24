#!/usr/bin/python3

def safe_print_integer_err(value):
    """
    A function that prints an integer.

    Args:
        value: The value to be printed.

    Returns:
        has_been_print: True if value has been correctly printed. (It means
            the value is an integer). Otherwise, returns False and prints in
            stderr the error precede by Exception:
    """
    import sys
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as e:
        sys.stderr.write("Exception: {}\n".format(e))
        return False
    else:
        return True
