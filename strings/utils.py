# -*- coding: utf-8 -*-
"""
    Utils
    -----

"""


def is_palindromic(value):
    """ Returns True if the given value is palindormic

    :param value: value of to analyze
    :type value: str
    :rtype: bool
    :returns: True if the value is palindromic
    """

    if not value:
        return False

    length = len(value)

    if length == 1:
        return True
    if length == 2 and value[0] == value[1]:
        return True

    low, high = 0, length - 1
    while low < high:
        if value[low] != value[high]:
            return False
        low += 1
        high -= 1
    return True
