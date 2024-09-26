"""
    LRU Cache
    ---------
    Design and implement a data structure for Least Recently Used (LRU)
    cache. It should support the following operations: get and put.

    get(key) - Get the value (will always be positive) of the key if the key
    exists in the cache, otherwise return -1.

    put(key, value) - Set or insert the value if the key is not already
    present. When the cache reached its capacity, it should invalidate the
    least recently used item before inserting a new item.

    The cache is initialized with a positive capacity.

"""

class Node():
    """ """
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList():
    """ """

    def __init__(self):
        """ """
        
        self.head = Node(None)


class LRUCache():
    """ LRU Cache """

    def __init__(self, capacity):
        """ """
        
        #: 
        self.tbl = {}
        self.cache = [None] * capacity
        self.capacity = capacity

    def get(self, key):
        """ """
        
        idx = self.tbl.get(key)
        if idx is None:
            return -1

        
        self.cache[0] = key
        self.tbl[key] = 0

        return self.cache[idx]

    def put(self, key, value):
        """ """

    
