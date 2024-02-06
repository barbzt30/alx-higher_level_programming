#!/usr/bin/python3
""" defines a square """


class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """
        initializes square
        Args:
        size: size of a side square
        """

        if type(size) is not int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                raise TypeError('size must be an integer')
            self.__size = size

            def area(self):
                """
                finds area of square
                Returns:
                the area of the square
                """

                return self.__size ** 2
