#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    A function that prints the first x elements of a list and only integers.

    Args:
        my_list: The given list.
        x: The number of elements to print from the given list.

    Returns:
        nb_print: The real number of integers printed.
    """
    nb_print = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_print += 1
        except ValueError as ve:
            continue
        except TypeError as te:
            continue
        except IndexError as ie:
            continue
    print()
    return nb_print
