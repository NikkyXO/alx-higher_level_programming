#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    deletes an element based on the key from a dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
