import pytest

from data_structures import BinarySearchTree, ValueExistInTree


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
