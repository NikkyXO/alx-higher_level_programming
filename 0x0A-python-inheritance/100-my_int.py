#!/usr/bin/python3


class MyInt(int):
    """Contrary rebel class of int"""

    def __eq__(self, n2):
        """Returns the opposite of __eq__"""
        return super().__ne__(n2)

    def __ne__(self, n2):
        """Returns the opposite of __ne__"""
        return super().__eq__(n2)
