#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    total = 0
    for r in range(x):
        try:
            print("{}".format(my_list[r]), end="")
            total += 1
        except IndexError:
            break
    print("")
    return (total)
