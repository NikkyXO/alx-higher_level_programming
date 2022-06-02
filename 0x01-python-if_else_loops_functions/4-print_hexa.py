#!/usr/bin/python3

def print_hexa(number):
    hex_str = '0123456789abcdef'
    tens = number // 16
    ones = number % 16

    if tens > 0:
        return hex_str[tens] + hex_str[ones]
    else:
        return hex_str[ones]


if __name__ == '__main__':
    for num in range(99):
        print('{:d} = 0x{}'.format(num, print_hexa(num)))


def get_hexa(number):
    hexstr = '0123456789abcdef'
    tens = number // 16
    ones = number % 16
    if tens > 0:
        return hexstr[tens] + hexstr[ones]
    else:
        return hexstr[ones]


if __name__ == '__main__':
    for number in range(99):
        print('{:d} = 0x{}'.format(number, get_hexa(number)))
