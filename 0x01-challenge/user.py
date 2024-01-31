#!/usr/bin/python3
"""
This module defines the User class
"""


class User:
    """
    The User class
    """

    def __init__(self):
        """Documentation"""
        self.__email = None

    @property
    def email(self):
        """The email getter"""
        return self.__email

    @email.setter
    def email(self, value):
        """The email setter"""
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
