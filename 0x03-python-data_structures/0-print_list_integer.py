#!/usr/bin/python3

def print_list_integer(my_list=[]):
    list_len = len(my_list)

    for i in range(list_len):
        print("{:d}".format(my_list[i]))
