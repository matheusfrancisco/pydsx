"""
A linked list is a linear collection of data elements,
whose order is not given by their physical placement in memory.
Instead, each element points to the next. It is a data structure
consisting of a collection of nodes that together represent a sequence.

An classic linked list in python my implementation:

List is:
  Head->|Node|->|Node|->|Node|->Tail

"""


class Node:
    def __init__(self, value, node=None):
        self.__value = value
        self.__next = node

    @property
    def value(self):
        return self.__value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node

    def __str__(self):
        return f"Node: {self.value}"


class SinglyLinkedList:
    def __init__(self, head=None):
        self._head = head
        self.__len = 0

    def __len__(self):
        return self.__len

    def append(self, value, first=True, tail=False):
        if value is None:
            return None
        if first and not tail:
            self._append_first(value)
        if tail:
            self._append_tail(value)

    def _append_first(self, value):
        """
          Complexity O(1)
        """

        tmp = Node(value)
        tmp.next = self._head
        self._head = tmp
        self.__len += 1

    def _append_tail(self, value):
        """
          Complexity O(1)

          Before:
            N1->N2->N3->N4->None

          After:
            N1->N2->N3->N4->Node(value)->None
        """
        if self.__len == 1:
            self._append_first(value)

        node = Node(value)
        current_head_node = self._head

        while current_head_node.next is not None:
            current_head_node = current_head_node.next

        node.next = current_head_node.next
        current_head_node.next = node
        self.__len += 1


__all__ = ["SinglyLinkedList"]
