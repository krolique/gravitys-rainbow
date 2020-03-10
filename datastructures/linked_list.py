"""
    Linked List
    ----------

"""

class Node():
    """ Node """

    def __init__(self, value=None, next=None):
        """ """
        self.value = value
        
        #:
        self.next = next

    def __repr__(self):
        """ """

        if self.next:
            return f'{self.value}->' + self.next.__repr__()
        else:
            return f'{self.value}->{self.next}'

class LinkedList():
    """ """
    
    def __init__(self):
        """ """

        self.size = -1
        self.head = None

    def __repr__(self):
        """ """
        
        if self.head:
            return f'{self.head.value}->' + self.head.next.__repr__()
        else:
            return f'{self.head.value}->{self.head.next}'

    def size(self):
        """ """

        return self.size

    def add_first(self, value):
        """ """

        if self.head is None:
            self.head = Node(value)
        pt = Node(value=value)
        pt.next = self.head
        self.head = pt
        self.size += 1

    def add_last(self, value):
        """ """
        
        pt = self.head
        while pt.next:
            pt = pt.next

        pt.next = Node(value=value)
        self.size += 1
        
    def del(self, target):
        """ """

        if not self.head:
            


def del_node(head, target):
    """ """

    pt = head
    if pt.value == target:
        return pt.next

    while pt.next:
        if pt.next.value == target:
            pt.next = pt.next.next
            return head
        pt = pt.next

    return head

