#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """
        deletes keys with a specific value in a dictionary
        If the value doesn’t exist, the dictionary won’t change
        All keys having the searched value have to be deleted
    """

    new_dict = dict(a_dictionary)
    for k, v in new_dict.items():
        if v == value:
            a_dictionary.pop(k)

    return a_dictionary
