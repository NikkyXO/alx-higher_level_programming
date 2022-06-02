#!/usr/bin/python3
import sys
import hidden_4 as hide

if __name__ != '__main__':
    exit()

for name in dir(hide):
    if name[0:2] != "__":
        print(name)
