#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    function that returns a new dictionary with all values multiplied by 2
    """
    if a_dictionary is not None:
         new_dict = dict(a_dictionary)
        for k, v in new_dict.items():
            new_dict[k] = v * 2

        return new_dict
