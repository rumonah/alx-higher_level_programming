#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    saf = 0
    for r in range(0, x):
        try:
            print("{:d}".format(my_list[r]), end="")
            saf += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (saf)
