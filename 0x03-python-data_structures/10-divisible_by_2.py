#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    rumzy_list = []
    if my_list:
        for orig in my_list:
            rumzy_list.append(False if orig % 2 else True)
        return rumzy_list
