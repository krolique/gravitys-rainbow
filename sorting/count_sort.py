# -*- coding: utf-8 -*-
"""
    Insertion Sort
    --------------
    A module that contains insertion sort

"""


def val_freq(values, init_value=0, upper_bound=10):
    """ Returns

    :param values:
    :type values: list
    :param init_value:
    :type init_value: obj
    :param upper_bound:
    :type upper_bound: int
    """

    freq = [init_value] * upper_bound
    for value in values:
        freq[value] += 1
    return freq


def one_digit_count_sort(values):
    """ """

    freq = val_freq(values=values, init_value=0, upper_bound=10)
    ordered = []
    for value, count in enumerate(freq):
        if not count:
            continue
        ordered.extend([value] * count)

    return ordered


def key_count_sort(values, sort_key, name_key):
    """ Returns

    This is not a stable sort for the sort. The order in which the
    name_key property will be inserted for equal values is not deterministic.
    To do so would force this sort to have a Big-O algorithmic complexity of:

    O(N + M*log(M))

    And that would defeat the purpose of using this sort which can do Big-O
    of O(N).

    I saw  this online at https://www.interviewcake.com/concept/python3/
    counting-sort.

    Example of a input data set

    > data = [
        {'type': 'macadamia nut cookie', 'price': 4},
        {'type': 'double chocolate cake', 'price': 8},
        {'type': 'chocolate chip cookie', 'price': 4},
        {'type': 'sugar cookie', 'price': 2},
        {'type': 'creme brulee', 'price': 9},
        {'type': 'chocolate souflee', 'price': 9},
        {'type': 'fruit tart', 'price': 6},
        {'type': 'brownie', 'price': 2},
        {'type': 'eclair', 'price': 9}
    ]
    > key_count_sort(values=data, sort_key='price', )

    :returns: sorted list of
    """

    sortable_map = {}
    for item in values:
        sort_key_val = item[sort_key]
        sort_name_val = item[name_key]

        if sortable_map.get(sort_key_val) is None:
            sortable_map[sort_key_val] = []

        sortable_map[sort_key_val].append(sort_name_val)

    key_freq = val_freq(values=sortable_map.keys(), init_value=0,
                        upper_bound=10)

    ordered = []
    for value, count in enumerate(key_freq):
        if not count:
            continue
        ordered.extend(ordered[value])

    return ordered
