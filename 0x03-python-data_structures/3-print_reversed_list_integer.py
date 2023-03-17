#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    A function that prints all integers of a list, in reverse order.
    """
    if my_list is None:
        pass
    else:
        my_list.reverse()
        for integer in my_list:
            print("{:d}".format(integer))
