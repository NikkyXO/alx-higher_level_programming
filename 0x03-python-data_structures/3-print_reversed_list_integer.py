#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    A function that prints all the integers of a list in reverse order
    """

    length = len(my_list) - 1

    while length >= 0:
        print("{:d}".format(my_list[length]))
        length -= 1
