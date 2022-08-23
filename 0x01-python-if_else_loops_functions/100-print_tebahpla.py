#!/usr/bin/python3
for letter in reversed(range(97, 123)):
    print("{:c}".format(letter if (ch % 2 == 0) else (ch - 32)), end='')
