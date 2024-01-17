#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = list.copy(my_list)
    rep = new_list.index(search)
    new_list[rep] = replace

    return new_list
