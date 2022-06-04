#!/usr/bin/python

def new_in_list(my_list, idx, element):
    """
    A function that replace an element in a list at a given index without modifying original list.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
