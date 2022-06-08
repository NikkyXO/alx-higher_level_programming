#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurences of an element by another in a new list
    """
    if my_list is not None:
        new_list = my_list[:]
        for i in range(len(my_list)):
            if my_list[i] == search:
                new_list[i] = replace
            return new_list
