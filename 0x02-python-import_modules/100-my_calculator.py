#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    def calc(a, op, b):
        if op == '+':
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif op == '-':
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        elif op == '*':
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        elif op == '/':
            print("{} {} {} = {}".format(a, op, b, div(a, b)))


    op = ['+', '-', '*', '/']

    arg_count = len(sys.argv) - 1
    if arg_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    if sys.argv[2] in op:
        calc(num1, sys.argv[2], num2)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
