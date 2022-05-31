#!/usr/bin/python3

def print_alpha_ex():
	for n in range(97, 123):
		if n != 101 and n != 123:
			print('{}'.format(chr(n)), end='')


if __name__ == '__main__':
	print_alpha_ex()
