#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    rumzy_dict = dict(a_dictionary)
    for r, x in rumzy_dict.items():
        rumzy_dict[r] = x * 2
        return rumzy_dict
