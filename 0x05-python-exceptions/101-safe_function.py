#!/usr/bin/python3

def safe_function(fct, *args):
    """
    A function that executes a function safely.

    Args:
        fct: A given function.
        *args: A tuple of arguments that the given funcion takes.

    Returns:
        result: The result of the function. Otherwise, returns None if
            something happens during the function and prints in stderr
            the error precede by Exception:
    """
    import sys
    try:
        result = fct(*args)
    except Exception as e:
        sys.stderr.write("Exception: {}\n".format(e))
        result = None

    return result
