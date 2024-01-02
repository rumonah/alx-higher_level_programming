#!/usr/bin/python3
for r in range(ord('a'), ord('z') + 1):
    if chr(r) != 'e' and chr(r) != 'q':
        print('{:c}'.format(r), end='')
