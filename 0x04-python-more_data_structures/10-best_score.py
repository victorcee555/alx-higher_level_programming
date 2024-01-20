#!/usr/bin/python3

def best_score(a_dictionary):
    max_number = 0
    max_key = ""
    if a_dictionary is not None:
        for key, num in a_dictionary.items():
            if num > max_number:
                max_number = num
                max_key = key

        return max_key
    else:
        return None
