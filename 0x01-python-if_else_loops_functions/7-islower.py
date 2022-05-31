#!/usr/bin/python3

def islower(c):
	ch = ord(c)
	if ch >= 97 and ch <= 122:
		return True
	else:
		return False


if __name__ == '__main__':
	print(islower('A'))
