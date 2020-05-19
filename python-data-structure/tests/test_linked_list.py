import pytest

from data_structures import SinglyLinkedList


@pytest.fixture()
def singly_linked_list():
    return SinglyLinkedList()


def test_initial_len_should_be_zero(singly_linked_list):
    assert len(singly_linked_list) == 0


# TODO split in many tests case
def test_linked_list_append_node():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(1)
    assert len(singly_linked_list) == 1
    singly_linked_list.append(3)
    assert singly_linked_list._head.value == 3
    assert singly_linked_list._head.next.value == 1
    assert len(singly_linked_list) == 2
    singly_linked_list.append(5)
    singly_linked_list.append(7, tail=True)
    assert singly_linked_list._head.value == 5
    assert singly_linked_list._head.next.next.next.value == 7
