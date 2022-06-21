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

    @property
    def size(self):
        """Call the function to checking property
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """check errors and setter for size attribute
        Args:
            value: Value to check Exception errors
        Raises:
            TypeError: Exception if size is not an integer
            ValueError: Exception if size is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    def my_print(self):
        """Print a square using # character
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end='')
                print()


if __name__ == '__main__':
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
