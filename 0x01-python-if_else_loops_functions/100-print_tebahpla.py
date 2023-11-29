#!/usr/bin/python3

for i in range(26, 0, -1):
    a = chr(i + 96)
    b = chr(i + 64)
    print("{}".format(a if i % 2 == 0 else b), end="")
