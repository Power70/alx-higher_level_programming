#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = len(sys.argv) - 1
    total = 0

    for i in range(arguments):
        total += int(sys.argv[i + 1])

    print("{:d}".format(total))
    