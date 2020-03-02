# Find an element in an array in better than linear time

Given an array of integers where each element is +1 or -1 than its
preceding element. Write a function to find an element in this array with
better than linear time.

What is better than linear time would be an excellent question because you
generally have O(1) and then O(n) while an algorithm may find something in
O(n-1) that may still be considered linear time. What we are trying to
achieve is a function that on the average will perform less than n
number of comparisons to find an element in the array.

```
    Given: [4, 5, 6, 7, 8, 9, 10, 9, 10], find first occurrence of 10
    Output: 6
```



# Solution

This searches the integer array by using the fact that the array is bounded
by a monotonic sequence increase in its values. The algorithm begins at
index 0 and compares the array value at the index to the desired number.
If the number is not found the index is incremented by subtracting current
index value from the desired number. The explanation of why this algorithm
work is as follows.

Let's run through an example of find 6 in the given array with the
described algorithm.

```
     ↓
    [1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]

```

Element at index 0 does not equal to 6, and we increment the index counter (6 - 1) by 5

```
                    ↓
    [1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]
```

Element at index 5 does not equal to 6, and we increment the index counter (6 - 2) by 4

```
                                ↓
    [1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6] index = 9
```

Element at index 9 does not equal to 6, and we increment the index counter (6 - 2) by 4

```
                                            ↓
    [1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6] index = 13
```

The element at index 13 does equal 6 and we can return 13

The algorithm seems to work, however how do we know this approach will not miss an element when an index is incremented?

Lets run through an example where we would fail to find a given number. Find 8 in the same array.

```
     ↓
    [1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]
```

Element at index 0 does not equal to 8, and we increment the index counter (8 - 1) by 7

```
                          ↓
    [1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6]
```

Element at index 7 does not equal to 8, and we increment the index counter (8 - 0) by 8

```
                                                   ↓
    [1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4, 5, 6], 7, 8
```

Oops, we are out of bound! Which means this array of integers cannot 
possibly contain the number we are searching for and we return -1.

The generalization can be made as: Every increase in the index by a - k
(where a is the desired number and k is the current index element value)
cannot miss the target number because the number cannot be inserted into
the array until +/- k values before it. Therefore we can increment the
index by this difference without missing the number. As you can see
although we didn't find our target number the algorithm did predict
correctly where the target would have been if the sequence was increasing.

What if you were given an array of integer where each element is +/- 3 of
preceding one? We then can adjust the a - k increment by dividing by 3.
Because now there are 3 less steps we have to make in every increment.

Example, find number 16 in the current array.

```
     ↓
    [1, 4, 7, 10, 13, 16, 13, 10, 7]
```

Element at index 0 does not equal to 16, and we increment the index counter by (16 - 1)/3 by 5

```
                      ↓
    [1, 4, 7, 10, 13, 16, 13, 10, 7]
```
The element at index 5 does equal 16 and we can return 5


```python

from math import fabs

def int_array_search(array, number_to_find):
    """Returns the index of the number we wish to find or -1 if the number is
    not in the array.

    :param array: a list of integers whose elements are +1 or -1 than the
    preceding element
    :type array: list
    :param number_to_find: the number we wish to find
    :type number_to_find: int
    :returns: the index of the number we wish to find or -1 if nothing is found
    """

    idx = 0
    while(idx < len(array)):
        if array[idx] == number_to_find:
            return idx
        idx += int(fabs(number_to_find - array[idx]))

    return -1

```
