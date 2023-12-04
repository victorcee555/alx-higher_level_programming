#!/usr/bin/python3

def multiple_returns(sentence):
    if sentence:
        tuple_ret = (len(sentence), sentence[0])
        return tuple_ret
    else:
        tuple_ret = (len(sentence), None)
        return tuple_ret
