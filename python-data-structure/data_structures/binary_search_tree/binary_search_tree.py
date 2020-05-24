class ValueExistInTree(Exception):
    def __init__(self, message):
        self.message = message


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree:
    """
      The left subtree of a node contains only nodes with keys lesser than
      the node’s key.
      The right subtree of a node contains only nodes with keys greater
      than the node’s key.
      The left and right subtree each must also be a binary search tree.
      There must be no duplicate nodes.

      example:
            8
           / \'
          3   10
         / \'  \'
        2   4  14

    """

    def __init__(self):
        self.root = None
        self._number_of_nodes = 0

    def height(self):
        if self.root is None:
            return 0
        else:
            return self._height(self.root)

    def _height(self, current_node):
        if current_node is None:
            return -1
        else:
            left_node = self._height(current_node.left)
            right_node = self._height(current_node.right)
            if left_node > right_node:
                return left_node + 1
            else:
                return right_node + 1

    def __len__(self):
        """
          Time complexity:
            Best case:
              O(1)
            Worst case:
              O(1)
        """
        return self._number_of_nodes

    def insert(self, data):
        """
          Time complexity:
            Best case:
              O(1)
            Worst case:
              O(1)
        """
        if self.root is None:
            self.root = Node(data)
            self._number_of_nodes += 1
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        """
          Time complexity:
            Best case:
              O(log n)

            Worst case:
              O(n)
        """
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
                self._number_of_nodes += 1
            else:
                self._insert(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = Node(data)
                self._number_of_nodes += 1
            else:
                self._insert(data, current_node.right)
        else:
            raise ValueExistInTree("Value is already in tree")


__all__ = ["BinarySearchTree", "ValueExistInTree"]
