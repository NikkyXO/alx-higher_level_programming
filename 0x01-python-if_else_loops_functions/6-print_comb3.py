#!/usr/bin/python3
for n in range(10):
    for j in range(n + 1, 10):
        if n == 8 and j == 9:
            print('{:d}{:d}'.format(n, j))
        else:
            print('{:d}{:d}'.format(n, j), end=', ')
