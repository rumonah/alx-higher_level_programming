#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = sorted(a_dictionary)
    for r in x:
        print("{}: {}".format(r, a_dictionary[r]))
