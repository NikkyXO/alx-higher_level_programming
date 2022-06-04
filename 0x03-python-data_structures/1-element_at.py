#!/usr/bin/python3
def element_at(my_list, idx):
    """
    A function that retrieves an element from a list
    """

    if idx >= len(my_list) or idx < 0:
        return None

    for i in my_list:
        if i == idx:
            return my_list[i]
