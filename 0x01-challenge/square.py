#!/usr/bin/python3
"""
This module defines a Square class
"""


class square:
    """
    The Square class
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Initializes a square"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Returns the area of the square"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """Returns the perimter of the square"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """Returns a string representation of the square"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
