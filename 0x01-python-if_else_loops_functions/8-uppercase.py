#!/usr/bin/python3

def uppercase(str):
    """
    A function that prints a string in uppercase.
    """
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            char = ord(str[i]) - 32
        else:
            char = ord(str[i])

        print("{:c}".format(char), end="")
    print()
