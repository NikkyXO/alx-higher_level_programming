#!/usr/bin/python3
import sys

if __name__ != '__main__':
    exit()

argc = len(sys.argv) - 1
argstr = "{:d} argument"

if argc == 0:
    argstr += 's.'

elif argc == 1:
    argstr += ':'

else:
    argstr += 's:'
print(argstr.format(argc))

i = 0
for argument in sys.argv:
    if i != 0:
        print(f"{i} {argument}")
    i += 1
