#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = new_dict.copy()
    for r, x in tmp.items():
        if value == x:
            new_dict.pop(r)
            return new_dict
