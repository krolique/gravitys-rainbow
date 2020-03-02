# -*- coding: utf-8 -*-
"""
    Addition
    --------
    A module that contains binary addition functions

"""


def add_str_binary(num_one, num_two):
    """ Returns binary string representation of adding two strings
    representing binary numbers

    :param num_one: binary string representation of the number to add
    :type num_one: str
    :param num_two: binary string representation of the number to add
    :type num_two: str
    :rtype: str
    :returns: string representing the binary number resulted in addition
    """

    max_len = max(len(num_one), len(num_two))
    v_num_one = list(map(int, list(num_one.zfill(max_len))))
    v_num_two = list(map(int, list(num_two.zfill(max_len))))
    sum_bits = [None] * max_len
    carry = 0

    for r_idx in reversed(range(max_len)):
        result = v_num_one[r_idx] ^ v_num_two[r_idx]
        if carry and not result:
            result = 1
            carry = 0

        if result and carry:
            result = 0
        else:
            carry = v_num_one[r_idx] & v_num_two[r_idx]

        sum_bits[r_idx] = result

    if carry:
        sum_bits.insert(0, carry)

    str_result = ''.join(map(str, sum_bits))
    assert str_result == bin(int(num_one, 2) + int(num_two, 2))[2:]
    return str_result
