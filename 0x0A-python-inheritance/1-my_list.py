#!/usr/bin/python3
"""Contains the Mylist Class"""


class MyList(list):
    """A subclass MyList that inherits from list"""

    def __init__(self):
        """Initialises the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
