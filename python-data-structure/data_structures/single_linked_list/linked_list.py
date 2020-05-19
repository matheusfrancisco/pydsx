"""
An classic linke list in python my implementation:

List is:
  |Node|->|Node|->|Node|

"""


class Node:
    def __init__(self, value, node=None):
        self.value = value
        self.next = node


class SingleLinkedList:
    def __inti__(self, node):
        pass


__all__ = ["SingleLinkedList"]
