# -*- coding: utf-8 -*-
"""
    Insertion Sort
    --------------

    Insertion sort is a simple sorting algorithm that builds the final sorted
    array (or list) one item at a time. It is much less efficient on large
    lists than more advanced algorithms such as quicksort, heapsort, or merge
    sort. However, insertion sort provides several advantages:


    1.  Simple implementation: Bentley shows a three-line C version, and a
        five-line optimized version[1]:116

    2.  Efficient for (quite) small data sets

    More efficient in practice than most other simple quadratic (i.e., O(n2))
    algorithms such as selection sort or bubble sort and usually faster in
    practice than asymptotically faster algorithms for small data sets

    Adaptive, i.e., efficient for data sets that are already substantially
    sorted: the time complexity is O(nk) when each element in the input is no
    more than k places away from its sorted position

    Stable; i.e., does not change the relative order of elements with equal
    keys In-place; i.e., only requires a constant amount O(1) of additional
    memory space Online; i.e., can sort a list as it receives it

         ↓
    [31, 41, 59, 26, 41, 58]

"""


def insertion_sort(array):
    """ """

    for idx in range(len(array)):
        while idx and array[idx - 1] >= array[idx]:
            array[idx], array[idx - 1], = array[idx - 1], array[idx]
            idx -= 1
