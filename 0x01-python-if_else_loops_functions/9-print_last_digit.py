#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        ld = number % -(10)
        print(-(ld), end='')
    else:
        ld = number % 10
        print(ld, end='')
    return abs(ld)
