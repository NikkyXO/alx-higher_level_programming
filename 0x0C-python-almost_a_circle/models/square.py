#!/usr/bin/python3

""" This module contains the class "square" """

from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """A representation of a square"""
        super().__init__(size, size, x, y, id)
        """Initializes a square"""
        self.size = size

    def __str__(self):
        """informal string representation of the square"""
        return "[Square] ({}) {}/{} - {} ".format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.size)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """**kwargs must be skipped if 
        *args exists and is not empty"""

        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Returns the dictionary representation of the square"""
        new_dic = {}
        new_dic["id"] = self.id
        new_dic["size"] = self.size
        new_dic["x"] = self.x
        new_dic["y"] = self.y
        return new_dic
