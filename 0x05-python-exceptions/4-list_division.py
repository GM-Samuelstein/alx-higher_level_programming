#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    A function that divides element by element 2 lists.

    Args:
        my_list_1: The first given list.
        my_list_2: The second given list.
        list_length: The length of the result list.
    
    Returns:
        result: A new list (length = list_length) with all divisions.
    """
    result = []
    for i in range(list_length):
        try:
            division_result = my_list_1[i] / my_list_2[i]
        except TypeError as te:
            print("wrong type")
            division_result = 0
        except ZeroDivisionError as zde:
            print("division by 0")
            division_result = 0
        except IndexError as ie:
            print("out of range")
            division_result = 0
        finally:
            result.append(division_result)

    return result
