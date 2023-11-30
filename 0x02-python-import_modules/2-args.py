#!/usr/bin/python3

import sys

if __name__ == "__main__":
        arg_count = len(sys.argv)
        if arg_count == 1:
            print("0 arguments.")
        elif arg_count == 2:
            print("1 argument:")
            print("1: {}".format(sys.argv[1]))
        elif arg_count > 2:
            print("{} arguments:".format(arg_count - 1))
            for i in range(len(sys.argv) - 1):
                print("{}: {}".format(i+1, sys.argv[i+1]))
