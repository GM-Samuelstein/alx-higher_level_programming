#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    n = len(sys.argv) - 1
    if n == 0:
        print(f"{n:d} arguments.")
    elif n == 1:
        print(f"{n:d} argument:")
    else:
        print(f"{n:d} arguments:")

    if n != 0:
        for i in range(len(sys.argv) - 1):
            print(f"{i + 1}: {sys.argv[i + 1]}")
