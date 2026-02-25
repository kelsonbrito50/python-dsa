from src.linked_lists.singly import SinglyLinkedList


def test_push_and_list():
    ll = SinglyLinkedList()
    ll.push(3)
    ll.push(2)
    ll.push(1)
    assert ll.to_list() == [1, 2, 3]


def test_reverse():
    ll = SinglyLinkedList()
    for i in [3, 2, 1]:
        ll.push(i)
    ll.reverse()
    assert ll.to_list() == [3, 2, 1]


def test_find():
    ll = SinglyLinkedList()
    ll.push(5)
    assert ll.find(5) is True
    assert ll.find(99) is False
