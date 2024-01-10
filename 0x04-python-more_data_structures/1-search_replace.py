#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rumzy_list = list(my_list)
    for x in range(len(rumzy_list)):
        if rumzy_list[x] == search:
            rumzy_list[x] = replace
            return rumzy_list
