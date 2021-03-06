"""
Defines the public API and the implementation of the Linked List data structure
"""
from .node import Node

class LinkedListEmptyException(Exception):
    def __init__(self, method_name):
        super(LinkedListEmptyException, self).__init__(None)
        self.method_name = method_name
    def __str__(self):
        return '%s() method can not be called on an empty List' % self.method_name

# pylint: disable=C0103
def raiseExceptionWhenListIsEmpty(function):
    def wrapper(self, *args):
        if self.is_empty():
            raise LinkedListEmptyException(function.__name__)
        else:
            return function(self, *args)

    return wrapper
# pylint: enable=C0103

class LinkedList(object):
    def __init__(self):
        super(LinkedList, self).__init__()
        self._head = None
        self._tail = None
        self._iter_head = None

    def __iter__(self):
        self._iter_head = self._head
        return self

    def next(self):
        if self._iter_head is None:
            raise StopIteration()
        else:
            node = self._iter_head
            self._iter_head = self._iter_head.next_node
            return node

    def push(self, payload):
        self._head = Node(payload, self._head)

        if self._tail is None:
            self._tail = self._head

        return self._head

    def push_tail(self, payload):
        new_tail = Node(payload)

        if self.is_empty():
            self._head = new_tail
        else:
            self._tail.next_node = new_tail

        self._tail = new_tail
        return new_tail

    @raiseExceptionWhenListIsEmpty
    def pop(self):
        old_head = self._head
        self._head = self._head.next_node
        return old_head.payload

    @raiseExceptionWhenListIsEmpty
    def head(self):
        return self._head.payload

    def is_empty(self):
        return self._head is None
