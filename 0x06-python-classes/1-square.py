#!/usr/bin/python3

class Square:
    """Square class."""

    def __init__(self, size):
        """__init__ method for Square.
        Args:
            size (int): size of Square.
        """
        self.__size = size


if __name__ == '__main__':
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
