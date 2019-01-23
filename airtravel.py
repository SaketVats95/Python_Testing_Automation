""" Model for aircraft flights"""


class Flight:

    def __init__(self, number):
        if not number[:2].isalpha():
            raise  ValueError("No air Line Code in '{}'".format(number))
        self._number = number

    def number(self):
        return self._number[:4]

