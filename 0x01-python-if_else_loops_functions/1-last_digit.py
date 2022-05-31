#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit = abs(number) % 10

if number < 0:
    last_digit = -last_digit
print(f"Last digit of {number} is {last_digit} and is ", end="")

if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")


def get_randn():
	number = random.randint(-10000, 10000)
	return number


def get_last_digit(number):
	if number >= 0:
		return number % 10
	else:
		if (number % 10) != 0:
			return 10 - (number % 10)
		else:
			return 0


def print_last_digit(last_digit):

	print('Last digit of {:d} is {:d}'.format(number, last_digit), end=' ')
	if last_digit > 5:
		print('{}'.format('and is greater than 5'))
	elif last_digit == 0:
		print('{}'.format('and is 0'))
	elif last_digit < 6 and last_digit != 0:
		print('{}'.format('and is less than 6 and not 0'))


if __name__ == '__main__':
	number = get_randn()
	last_digit = get_last_digit(number)
	print_last_digit(last_digit)
