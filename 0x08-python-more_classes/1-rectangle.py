#!/usr/bin/python3
"""This is the "1-rectangle" module
It supplies A class "Rectangle"
"""


class Rectangle():
    """class Rectangle that defines a rectangle figure
    Attributes:
        empty
    """

    def __init__(self, width=0, height=0):
        """init method for class Rectangle
        Attributes:
            width(int): the width of the rectangle
            heigth(int): the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Property width to retrieve it

        Returns:
            width (int): the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter width of rectangle

        Attributes:
            width(int): The width of the rectangle
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        Property height to retrieve it

        Returns:
            height (int): the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter width of rectangle

        Attributes:
            width(int): The width of the rectangle
        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value


if __name__ == '__main__':
    my_rectangle = Rectangle(2, 4)
    print(my_rectangle.__dict__)

    my_rectangle.width = 10
    my_rectangle.height = 3
    print(my_rectangle.__dict__)
