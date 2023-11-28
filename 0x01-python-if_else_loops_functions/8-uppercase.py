#!/usr/bin/python3

def uppercase(str):
    for i in str:
        c = ord(i)
        d = chr(c - 32)

        print("{}".format(d if c > 96 and c < 124 else i), end="")
    print("\n", end="")
