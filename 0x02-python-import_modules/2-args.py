#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args_num = len(sys.argv) - 1

    print(
            "{:d} argument".format(args_num)
            if args_num == 1 else "{:d} arguments".format(args_num), end=""
        )
    print("." if args_num == 0 else ":")
    for i in range(1, args_num + 1):
        print("{:d}: {}".format(i, sys.argv[i]))
        