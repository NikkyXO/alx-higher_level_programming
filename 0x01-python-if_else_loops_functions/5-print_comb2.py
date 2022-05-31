#!/usr/bin/python3

def print_num_in_range_100():
	for n in range(100):
		if n != 99:
			print('{:02d}'.format(n), end=', ')
		else:
			print('{:02d}'.format(n))


if __name__ == '__main__':
	print_num_in_range_100()
