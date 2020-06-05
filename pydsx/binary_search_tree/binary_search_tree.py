from pydsx import SinglyLinkedList


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

      - [ ] TODO implement iterative insert
      - [ ] TODO implement iterative max depth or height
      - [ ] TODO implement iterative search node
      - [ ] TODO improve remove method
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

          This is a recursive insert
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

    def search(self, value):
        """
          Time complexity:
            Best case: O(1) O(log n)
            Worst case: O(n)

        """
        return self._search(self.root, value)

    def _search(self, root, value):
        """
          Time complexity:
            Best case: O(1) O(log n)
            Worst case: O(n)

        """
        if root is None or root.data == value:
            return root

        if root.data < value:
            return self._search(root.right, value)
        return self._search(root.left, value)

    def _get_lowest_node(self, current_node):
        """
          Time complexity:
            Best case: O(n)
            Worst case: O(n)

          This is called inorder
        """
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def remove(self, value):
        """
          Time complexity:
            Best case: O(1) O(log n)
            Worst case: O(n)

        """
        return self._remove(self.root, value)

    def _remove(self, root, value):
        """
          Time complexity:
            Best case: O(log n)
            Worst case: O(n)

          To think in this algorithms
          thinked in tree cases:
          first: remove value 3
              4
             / \'
            3   5

          second: remove value 6
              4
             / \'
            3   6
               /
              5
          thrid: remove 4
              4
             / \'
            3   6
               / \'
              5   7
        """
        if root is None:
            if self._number_of_nodes == 0:
                return root
            self._number_of_nodes -= 1
            return root
        if value < root.data:
            root.left = self._remove(root.left, value)
        elif value > root.data:
            root.right = self._remove(root.right, value)
        else:
            if root.left is None:
                aux_node = root.right
                root = None
                return aux_node
            elif root.right is None:
                aux_node = root.left
                root = None
                return aux_node
            temp = self._get_lowest_node(root.right)
            root.data = temp.data
            root.right = self._remove(root.right, temp.data)
        self._number_of_nodes -= 1
        return root

    def inorder(self):
        """
          Time complexity:
            Best case: O(n)
            Worst case: O(n)
        """
        singly_linked_list = SinglyLinkedList()
        return self._inorder(self.root, singly_linked_list)

    def _inorder(self, root, singly_linked_list):
        """
          Time complexity:
            Best case: O(n)
            Worst case: O(n)

        TODO see append tail in when list is empty
        """
        if root is not None:
            self._inorder(root.left, singly_linked_list)
            if len(singly_linked_list) >= 1:
                singly_linked_list.append(root.data, first=False, tail=True)
            else:
                singly_linked_list.append(root.data)
            self._inorder(root.right, singly_linked_list)
        return singly_linked_list

    def pre_order(self):
        """
          Time complexity:
            Best case: O(n)
            Worst case: O(n)
        """
        singly_linked_list = SinglyLinkedList()
        return self._pre_order(self.root, singly_linked_list)

    def _pre_order(self, root, singly_linked_list):
        """
          Time complexity:
            Best case: O(n)
            Worst case: O(n)

        """
        if root is not None:
            singly_linked_list.append(root.data)
            self._pre_order(root.left, singly_linked_list)
            self._pre_order(root.right, singly_linked_list)
        return singly_linked_list


__all__ = ["BinarySearchTree", "ValueExistInTree"]
