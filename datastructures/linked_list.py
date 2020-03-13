# -*- coding: utf-8 -*-
"""
    Linked List
    -----------

    In computer science, a linked list is a linear collection of data
    elements, whose order is not given by their physical placement in
    memory. Instead, each element points to the next.

    It is a data structure consisting of a collection of nodes which
    together represent a sequence. In its most basic form, each node
    contains: data, and a reference (in other words, a link) to the
    next node in the sequence. This structure allows for efficient
    insertion or removal of elements from any position in the sequence
    during iteration.

    More complex variants add additional links, allowing more
    efficient insertion or removal of nodes at arbitrary positions.
    A drawback of linked lists is that access time is linear
    (and difficult to pipeline). Faster access, such as random access,
    is not feasible.

    Time complexity:
    +---------------+--------+--------+-----------+----------+
    | Type          | Access | Search | Insertion | Deletion |
    |---------------+--------+--------+-----------+----------+
    | Singly-Linked | Θ(n)   | Θ(n)   | Θ(1)      | Θ(1)     |
    +---------------+--------+--------+-----------+----------+

    Space complexity:
    +---------------+-------------------+
    | Type          | Space Complexity  |
    +---------------+-------------------+
    | Singly-Linked | O(n)              |
    +---------------+-------------------+

"""

from node import LinkedNode


class LinkedList():
    """ Linked List """

    def __init__(self):
        """ Creates a new instance of the LinkedList class"""

        #: defines the number of nodes in the list
        self.size = 0

        #: defines the reference to the head
        self.head = None

    def __repr__(self):
        """ Returns visual representation of the LinkedList class

        complexity: O(n)

        :rtype: str
        """

        return self.head.__repr__() or 'Empty'

    def size(self):
        """ Returns the size of the linked list

        complexity: O(1)

        :rtype: int
        """

        return self.size

    def clear(self):
        """ Removes all of the elements from this list.

        complexity: O(1)
        """

        self.head = None
        self.size = 0

    def add_first(self, value):
        """ Inserts the specified element at the beginning of this
        list.

        complexity: O(1)

        :param value: the value to insert
        :type value: obj
        """

        if self.head is None:
            self.head = LinkedNode(value)
        else:
            pt = LinkedNode(value=value)
            pt.next = self.head
            self.head = pt

        self.size += 1

    def add_last(self, value):
        """ Appends the specified element to the end of this list.

        complexity: O(n)

        :param value: the value to insert
        :type value: obj
        """

        pt = self.head
        while pt.next:
            pt = pt.next

        pt.next = LinkedNode(value=value)
        self.size += 1

    def _ensure_index(self, index):
        """ Ensures the index value is within the range of the list
        otherwise raises an IndexError exception

        :para index: the value of the index to evaluate
        :type index: int
        """

        if index < 0 or index > self.size:
            raise IndexError('the index is out of range (index < 0 '
                             f'|| index > {self.size})')

    def add_index(self, value, index):
        """ Inserts the specified element at the specified position in
        this list.

        complexity: O(n)

        :param value: the value to insert
        :type value: obj
        :param index: the index in the list to insert the element at
        :type index: int
        """

        self._ensure_index(index=index)

        if index == 0:
            self.add_first(value)
        pt, cnt = self.head, 1
        while pt.next:
            if cnt == index:
                new_node = LinkedNode(value=value)
                tmp = pt.next
                pt.next = new_node
                new_node.next = tmp
                self.size += 1
                return
            pt = pt.next
            cnt += 1

    def remove_last(self):
        """ Removes and returns the last element from this list."""

        if not self.head:
            return

        if not self.head.next:
            target = self.head
            target.next = None
            self.head = None
            self.size -= 1
            return target

        pt = self.head
        while pt.next:
            pt = pt.next
            if pt.next is None:
                pt


    def remove_index(self, index):
        """ Removes the element at the specified position in this list.

        :param index: the index in the list to remove the element from
        :type index: int
        """

        self._ensure_index(index=index)

        pt, cnt = self.head, 0
        while pt:
            if cnt == index:
                target = pt
                self.head = self.head.next
                target.next = None
                self.size -= 1
                return target
            pt = pt.next

    def remove_value(self, value):
        """ Removes the first occurrence of the specified element from
        this list, if it is present.

        complexity: O(n)

        :param value: value of the object to remove
        :type value: obj
        :rtype: bool
        """

        if not self.head:
            return False

        pt = self.head
        if pt.value == value:
            self.head = pt.next
            self.size -= 1
            return True

        while pt.next:
            if pt.next.value == value:
                pt.next = pt.next.next
                self.size -= 1
                return True
            pt = pt.next

        return False
