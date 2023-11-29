#!/usr/bin/python3

for i in range(26, 0, -1):
    if i % 2 == 0:
        print(chr(i + 96), end="")
    else:
        print(chr(i + 64), end="")
