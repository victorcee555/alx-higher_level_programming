#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    new_list = []
    for i in a_dictionary.keys():
        new_list.append(i)
    new_list.sort()
    for i in new_list:
        print(i, ":", a_dictionary[i])
