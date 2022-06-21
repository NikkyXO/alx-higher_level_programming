#!/usr/bin/python3

class Square:
    """Class Square that has attributes. Instantiation with size
    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size=0):
        """The __init__ method for Square class
        Args:
            size: (:obj: 'int', optional): A private instance size
        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square
        Returns:
            The square area
        """
        return self.__size ** 2


if __name__ == '__main__':
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
