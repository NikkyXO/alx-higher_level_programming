#!/usr/bin/python3
"""This module defines an empty class BAseGeometry"""


class BaseGeometry:
    """A class with a public attribute area"""

    def area(self):
        """Raises an exception when called"""
        raise Exception("area() is not implemented")
