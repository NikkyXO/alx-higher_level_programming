#!/usr/bin/python3
"""This module contains a class BaseGeometry"""


class BaseGeometry:
    """A class with a public attribute area"""

    def area(self):
        """Raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value is an integer greater than 0"""
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
