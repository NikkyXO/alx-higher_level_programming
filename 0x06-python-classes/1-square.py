#!/usr/bin/python3

class Square:

    """A class Square that defines a square
    """

    def __init__self(self, size):
        """init method for class square

        Args: size (int): size of square
        """
        self.__size = size


if __name__ == '__main__':
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
