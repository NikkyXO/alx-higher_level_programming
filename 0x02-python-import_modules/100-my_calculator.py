#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ != '__main__':
    exit()

argc = len(argv) - 1

if argc != 3:
    print(f"Usage:{argv[0]} <a> <operator> <b>")
    exit(1)
elif argv[2] == '+':
    result = add(int(argv[1]), int(argv[3]))
elif argv[2] == '-':
    result = sub(int(argv[1]), int(argv[3]))
elif argv[2] == '/':
    result = div(int(argv[1]), int(argv[3]))
elif argv[2] == '*':
    result = mul(int(argv[1]), int(argv[3]))
else:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
print(f"{argv[1]} {argv[2]} {argv[3]} = {result}")
