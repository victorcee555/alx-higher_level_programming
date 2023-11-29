#!/usr/bin/python3

for i in range(26, 0, -1):
        print(chr(i + 96) if i % 2 == 0 else chr(i + 64), end="")
