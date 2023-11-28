#!/usr/bin/python3

for i in range(10):
    for j in range(i, 10):
        k = j + 1

        if (i == 8):
            print("{}{}".format(i, k), end="\n")
            break
        if (k == 10):
            continue
        print("{}{}".format(i, k), end=", ")
