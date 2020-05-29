import pytest

from data_structures import BinarySearchTree, ValueExistInTree
from data_structures import SinglyLinkedList


"""
Improve test

- [ ] Remove duplicate code and create a fixture
- [ ] Write more test case

"""


@pytest.fixture()
def bst():
    return BinarySearchTree()


def test_initial_number_of_nodes(bst):
    assert len(bst) == 0


def test_initial_height_should_be_zero(bst):
    assert bst.height() == 0


def test_insert_4_child_assert_height_and_len(bst):
    bst.insert(8)
    bst.insert(3)
    bst.insert(1)
    bst.insert(4)
    assert len(bst) == 4
    assert bst.height() == 2


def test_insert_three_child_and_assert_the_order(bst):
    bst.insert(8)
    bst.insert(3)
    bst.insert(1)
    bst.insert(4)
    assert bst.root.data == 8
    assert bst.root.left.data == 3
    assert bst.root.left.left.data == 1
    assert bst.root.left.right.data == 4


def test_insert_some_child_and_assert_the_height(bst):
    bst.insert(8)
    bst.insert(10)
    bst.insert(3)
    bst.insert(1)
    bst.insert(4)
    assert len(bst) == 5
    assert bst.height() == 2


def test_should_raise_values_exist_in_tree(bst):
    bst.insert(8)
    bst.insert(10)
    bst.insert(3)
    bst.insert(1)
    bst.insert(4)
    with pytest.raises(ValueExistInTree):
        bst.insert(10)


def test_should_find_node_with_value(bst):
    bst.insert(8)
    bst.insert(10)
    bst.insert(3)
    bst.insert(1)
    bst.insert(4)
    node = bst.search(4)
    assert node.data == 4


def test_remove_value_from_tree(bst):
    bst.insert(8)
    bst.insert(10)
    bst.insert(3)
    bst_new_without_value_removed = bst.remove(8)
    assert bst_new_without_value_removed.data == 10
    assert bst_new_without_value_removed.left.data == 3
    assert bst_new_without_value_removed.right is None
    assert len(bst) == 2


def test_get_an_inorder_list_using_data_structure_list(bst):
    """
      trying to implement a different design for in order
      WIP IDEA
    """
    singly_linked_list = SinglyLinkedList()
    bst.insert(8)
    bst.insert(10)
    bst.insert(3)
    bst.insert(1)
    bst.insert(4)

    singly_linked_list.append(1, first=True)
    singly_linked_list.append(3, first=False, tail=True)
    singly_linked_list.append(4, first=False, tail=True)
    singly_linked_list.append(8, first=False, tail=True)
    singly_linked_list.append(10, first=False, tail=True)

    inorder_linked_list = bst.inorder()

    # compare itens
    # TODO I think this compare was too hard to understand refactor this
    has_equal_values = all(
        map(
            lambda x: x[0] == x[1], zip(singly_linked_list, inorder_linked_list)
        )  # noqa
    )

    assert has_equal_values is True
