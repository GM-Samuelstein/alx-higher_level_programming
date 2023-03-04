#!/usr/bin/python3
for number in range(90, 64, -1):
    if number % 2 == 0:
        number = number + 32
    else:
        number = number
    print("{:c}".format(number), end="")
