#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

def calculator():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    if not (a.isdigit() or (a[1:].isdigit() and a[0] == '-')):
        print("Invalid value for <a>")
        sys.exit(1)

    if not (b.isdigit() or (b[1:].isdigit() and b[0] == '-')):
        print("Invalid value for <b>")
        sys.exit(1)

    a, b = int(a), int(b)

    if operator not in {'+', '-', '*', '/'}:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == '+':
        result = add(a, b)
    elif operator == '-':
        result = sub(a, b)
    elif operator == '*':
        result = mul(a, b)
    elif operator == '/':
        if b == 0:
            print("Error: Division by zero")
            sys.exit(1)
        result = div(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == "__main__":
    calculator()

