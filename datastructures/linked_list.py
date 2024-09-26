"""
    Linked List
    ----------

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

        if self.head:
            return self.head.__repr__()

    def size(self):
        """ Returns the size of the linked list

        complexity: O(1)

        :rtype: int
        """

        return self.size

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
        :param index: zero based integer value of the values index in
                      the list
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

    def remove(self, value):
        """ Removes the first occurrence of the specified element from
        this list, if it is present.

        complexity: O(n)

        :param value: value of the object to remove
        :type value: obj
        """

        pt = self.head
        if pt.value == value:
            self.head = pt.next

        while pt.next:
            if pt.next.value == value:
                pt.next = pt.next.next
                return True
            pt = pt.next

        return False
