#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    for arg in range(len(sys.argv)):
        if arg == 0:
            continue
        else:
            sum = sum + int(sys.argv[arg])
    print(sum)
