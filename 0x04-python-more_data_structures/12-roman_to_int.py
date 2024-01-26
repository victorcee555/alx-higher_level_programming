#!/usr/bin/python3

def numeral_value(list_string):
    list_values = []
    index = 0

    for i in list_string:
        if i == 'I':
            list_values.append(1)
        elif i == 'V':
            list_values.append(5)
        elif i == 'X':
            list_values.append(10)
        elif i == 'L':
            list_values.append(50)
        elif i == 'C':
            list_values.append(100)
        elif i == 'D':
            list_values.append(500)
        elif i == 'M':
            list_values.append(1000)
        else:
            list_values = 0
        index += 1

    if len(list_values) > 1:
        if list_values[0] < list_values[1]:
            list_values[1] = list_values[1] - list_values[0]
            list_values[0] = 0
    return list_values


def roman_to_int(roman_string):
    I, V, X, L, C, D, M = 1, 5, 10, 50, 100, 500, 1000
    list_str = []
    value = 0
    

    if len(roman_string) != 0 or roman_string != None:
        for i in roman_string:
            list_str.append(i)

        value = sum(numeral_value(list_str))
        return value
    else:
        return 0
