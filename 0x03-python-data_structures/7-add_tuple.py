#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    siz_a, siz_b = len(tuple_a), len(tuple_b)
    new_tuple = ((tuple_a[0] if siz_a >= 1 else 0) +
                 (tuple_b[0] if siz_b >= 1 else 0),
                 (tuple_a[1] if siz_a >= 2 else 0) +
                 (tuple_b[1] if siz_b >= 2 else 0))
    return new_tuple
