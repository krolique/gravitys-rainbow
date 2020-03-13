# -*- coding: utf-8 -*-
"""
    Palindrome Linked List
    ----------------------
    This is an interesting solution to determining if a given
    linked list is a palindrome using two-pointers and recursion.

    source:
    https://leetcode.com/problems/palindrome-linked-list/solution/

"""


def is_palindrome(root):
    """ Returns True if the linked list, represented by a reference
    to the root of the list, is a palindrome.

    Example of a valid palindrome linked list:

        1->2->2->1

    The shape of each node in both the **root** and **f_pt** must
    have "value" and "next" defined in order for this function to
    work. As an example here is what the node class must be
    defined as:

    ```python
            class Node():
                def __init__(self, value):
                    self.value = value
                    self.next = None
    ```

    complexity: O(n)
    space complexity: O(n)

    Space complexity is O(n) because of the recursion and n number of
    call stacks created at run time.

    :param root: reference to the root node of the linked list
    :type root: cls
    :rtype: bool
    :returns: True if a linked list is a palindrome
    """

    def _is_pali(root, f_pt):
        """ Returns True if a linked list is palindrome.

        Iterates the root node forward until the linked list is
        consumed entirely. When the forward recursion is exhausted
        returns the call stack back to the function and begins to
        forward the other root node. At this point the two pointers
        will be used to compare values. One from the backtracking
        recusrion and the other from the forward.

        Example of the state when the condition of consuming the
        first root pointer:
        ```
                    root pointer
                     ↓
            1->2->3->4->None
            ↑
            f_pt pointer
        ```

        The idea of recursion use in this case comes from the
        post-order binary tree trivesals.

        :param root: reference to the root node of the linked list
        :type root: cls
        :param f_pt: reference to the root node of the linked list
        :type f_pt: cls
        """
        if root is not None:
            if not _is_pali(root.next):
                return False
            if f_pt.value != root.value:
                return False
            f_pt = f_pt.next
        return True

    return _is_pali(root=root, f_pt=root)
