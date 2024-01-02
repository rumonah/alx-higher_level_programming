#!/usr/bin/python3
for r in range(0, 10):
    for j in range(r + 1, 10):
        if r == 8 and j == 9:
            print('89')
        else:
            print('{}{}, '.format(r, j), end='')
