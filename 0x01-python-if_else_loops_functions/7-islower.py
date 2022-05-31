#!/usr/bin/python3
def islower(c):
<<<<<<< HEAD
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
=======
	ch = ord(c)
	if ch >= 97 and ch <= 122:
		return True
	else:
		return False


if __name__ == '__main__':
	print(islower('A'))
>>>>>>> 679dacaec727d19e38af7f43f4ef8d2cfa5d558e
