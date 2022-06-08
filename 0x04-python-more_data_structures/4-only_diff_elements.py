#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """ Returns a set of all elements present in only one set."""
    if set_1 is not None and set_2 is not None:
        return set_1 ^ set_2
