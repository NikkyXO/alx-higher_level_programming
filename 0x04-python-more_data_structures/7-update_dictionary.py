#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
        Replaces or adds key/value in a dictionary
        key argument will be always a string
        value argument will be any type
        If a key exists in the dictionary, the value will be replaced
        If a key doesn’t exist in the dictionary, it will be created
        You are not allowed to import any module
    """
    if a_dictionary is not None:
        new_dict = a_dictionary
        new_dict[key] = value
        return new_dict
