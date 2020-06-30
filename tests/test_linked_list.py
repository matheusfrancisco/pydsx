import pytest

from pydsx import SinglyLinkedList


@pytest.fixture()
def singly_linked_list():
    return SinglyLinkedList()


def test_initial_len_should_be_zero(singly_linked_list):
    assert len(singly_linked_list) == 0


def test_compare_values_iterate_at_singly_linked_list(singly_linked_list):
    singly_linked_list.append(3)
    singly_linked_list.append(2)
    singly_linked_list.append(1)

    list_to_compare = [1, 2, 3]

    has_same_size = len(list_to_compare) == len(singly_linked_list)
    has_equal_values = all(
        map(lambda x: x[0] == x[1], zip(singly_linked_list, list_to_compare))
    )

    assert has_same_size is True
    assert has_equal_values is True


def test_should_append_in_first_and_get_by_index(singly_linked_list):
    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.append(3)
    singly_linked_list.append(4)

    assert singly_linked_list.get(0) == 4
    assert singly_linked_list.get(1) == 3
    assert singly_linked_list.get(2) == 2
    assert singly_linked_list.get(3) == 1


def test_raise_index_error_when_index_is_out_off_range(singly_linked_list):
    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.append(3)
    singly_linked_list.append(4)

    with pytest.raises(IndexError):
        singly_linked_list.get(100)


def test_should_popped_first_element_from_linked_list(singly_linked_list):
    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.append(3)
    singly_linked_list.append(4)

    popped_value = singly_linked_list.pop()

    assert popped_value == 4

    assert singly_linked_list.get(0) == 3
    assert singly_linked_list.get(1) == 2
    assert singly_linked_list.get(2) == 1


def test_change_data_in_particular_node(singly_linked_list):
    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.append(3)
    singly_linked_list.append(4)

    singly_linked_list[1] = 5
    assert singly_linked_list.get(1) == 5


def test_raises_when_change_value_out_of_range(singly_linked_list):
    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.append(3)
    singly_linked_list.append(4)

    with pytest.raises(IndexError):
        singly_linked_list[5] = 5


def test_raises_list_is_empty(singly_linked_list):
    with pytest.raises(IndexError):
        singly_linked_list[5] = 5


# TODO Implement remove from singly linked list
def test_should_remove_element_from_linked_list(singly_linked_list):
    singly_linked_list.append(1)
    singly_linked_list.append(2)
    singly_linked_list.append(3)
    singly_linked_list.append(4)

    with pytest.raises(NotImplementedError):
        singly_linked_list.remove(0)


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


# Test append with tail flag
def test_append_with_tail_flag():
    singly_linked_list = SinglyLinkedList()
    singly_linked_list.append(1, tail=True)
    assert len(singly_linked_list) == 1
    assert singly_linked_list._head.value == 1
    singly_linked_list.append(7, tail=True)
    assert len(singly_linked_list) == 2
    assert singly_linked_list._head.next.value == 7


# Test merge_sort
def test_reverse_merge_sort():
    l = SinglyLinkedList()  # noqa
    l.append(6)
    l.append(1)
    l.append(2)
    l.append(4)
    l.append(8)
    l.append(9)
    l.append(5)
    l.append(7)
    l.append(3)
    l = l.sort()  # noqa
    list_to_compare = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    has_equal_values = all(map(lambda x: x[0] == x[1], zip(l, list_to_compare)))  # noqa
    assert has_equal_values is True


# Test merge_sort with reverse flag
def test_merge_sort():
    l = SinglyLinkedList()  # noqa
    l.append(6)
    l.append(1)
    l.append(2)
    l.append(4)
    l.append(8)
    l.append(9)
    l.append(5)
    l.append(7)
    l.append(3)
    l = l.sort(reverse=True)  # noqa
    list_to_compare = [9, 8, 7, 6, 5, 4, 3, 2, 1]

    has_equal_values = all(map(lambda x: x[0] == x[1], zip(l, list_to_compare)))  # noqa
    assert has_equal_values is True
