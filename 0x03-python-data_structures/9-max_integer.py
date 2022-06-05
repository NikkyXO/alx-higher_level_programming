#!/usr/bin/python3

def max_integer(my_list=[]):
    """ 
    finds the largest integer of a list
    """

    if len(my_list) == 0:
        return (None)

    max_int = my_list[len(my_list)-1]
    for i in range(len(my_list)):
        if my_list[i] > max_int:
            max_int = my_list[i]
    return (max_int)
