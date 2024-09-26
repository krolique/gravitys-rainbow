# -*- coding: utf-8 -*-
"""
    Node
    ----
    Contains classes and functions relating to node(s)

"""


class Node():
    """ Node
    A node is a basic unit of a data structure, such as a linked list
    or tree data structure. Nodes contain data and also may link to
    other nodes.
    """

    def __init__(self, value=None):
        """ Create a new instance of the node class

        :param value: the value this node contains
        :type value: obj
        """

        #: defines the value for the node
        self.value = value


class LinkedNode(Node):
    """ Linked Node
    A linked node is a basic unit of that has a value and a reference
    (pointer) to the next linked node.
    """

    def __init__(self, value=None, next=None):
        """ Create a new instance of the node class

        :param value: the value this node contains
        :type value: obj
        :param next: a reference to the next Node
        :type next: obj
        """

        super.__init__(value=value)

        #: defines the next node class in the chain
        self.next = next

    def __repr__(self):
        """ Returns visual representation of the Node class

        *note* - this function call is recursive and will trigger
        every self.next class to return its value. the output
        should look like this:
                1->2->3->4.....(n)

        complexity: O(n)

        :rtype: str
        """

        if self.next:
            return f'{self.value}->' + self.next.__repr__()
        else:
            return f'{self.value}->{self.next}'
