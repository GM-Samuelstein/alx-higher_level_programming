#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    A function that prints x elements of a list.

    Args:
        my_list: The given list, which can contain any type.
        x: The number of elements to be printed.

    Returns:
        nb_print: The real number of elements printed.

    """
    nb_print = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            nb_print += 1
        except IndexError:
            continue
    print("")
    return nb_print
