#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    A function that finds all multiples of 2 in a list.
    """
    list_result = []
    for item in my_list:
        if item % 2 == 0:
            list_result.append(True)
        else:
            list_result.append(False)
    
    return list_result
