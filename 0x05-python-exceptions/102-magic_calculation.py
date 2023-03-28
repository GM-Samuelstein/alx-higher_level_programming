#!/usr/bin/python3

def magic_calculation(a, b):
    """
    A python function that does exactly the same as a given python bytecode.
    """
    result = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except Exception:
            result = b + a

    return result
