#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
<<<<<<< HEAD
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
=======
    print("{:d} is positive".format(number))
elif number == 0:
    print("{:d} is zero".format(number))
else:
    print("{:d} is negative".format(number))
>>>>>>> 679dacaec727d19e38af7f43f4ef8d2cfa5d558e
