#!/usr/bin/python3
from magic_calculation_102 import add, sub


def magic_calculation(a, b):
    if a < b:
        k = add(a, b)
        for r in range(4, 6):
            k = add(k, r)
        return (k)
    else:
        return sub(a, b)
