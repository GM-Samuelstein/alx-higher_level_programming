#!/usr/bin/python3

def fizzbuzz():
    """
    A python function that prints the numbers from 1 to 100.

    Multiples of three are printed as Fizz, multiples of
    five are printed as Buzz, while multiples of both three and five
    are printed as FizzBuzz.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
