#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    A function that converts a Roman numeral to an integer.

    Args:
        roman_string: A roman numeral string.

    Returns:
        roman_integer: An integer equivalent in value to the given roman
            numeral.
    """
    if not isinstance(roman_string, str):
        return 0

    roman_numeral_dict = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    roman_numeral_list = []

    for char in roman_string:
        roman_numeral_list.append(roman_numeral_dict.get(char))

    smallest_integer = 10000
    for index in range(len(roman_numeral_list)):
        if roman_numeral_list[index] <= smallest_integer:
            smallest_integer = roman_numeral_list[index]
        else:
            roman_numeral_list[(index - 1)] = smallest_integer * -1
            smallest_integer = roman_numeral_list[index]

    roman_integer = 0
    for integer in roman_numeral_list:
        roman_integer += integer

    return roman_integer
