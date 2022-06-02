#!/usr/bin/python3
from sys import argv

if __name__ != '__main__':
    exit()

sum = 0

for i, argument in enumerate(argv[1:]):
    sum += int(argument)
print(f"{sum}")
