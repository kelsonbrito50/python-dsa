"""Tests for linked list cycle detection (Floyd's algorithm)."""

from src.linked_lists.detect_cycle import (
    ListNode,
    cycle_length,
    find_cycle_start,
    has_cycle,
)


def _make_list(vals: list[int]) -> ListNode | None:
    """Build a singly linked list from values."""
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def _make_cyclic(vals: list[int], cycle_index: int) -> ListNode:
    """Build a list where tail.next points to node at cycle_index."""
    head = _make_list(vals)
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next
    nodes[-1].next = nodes[cycle_index]
    return head


# --- has_cycle ---

def test_no_cycle_empty():
    assert has_cycle(None) is False


def test_no_cycle_single():
    assert has_cycle(ListNode(1)) is False


def test_no_cycle_multiple():
    assert has_cycle(_make_list([1, 2, 3, 4, 5])) is False


def test_cycle_self_loop():
    node = ListNode(1)
    node.next = node
    assert has_cycle(node) is True


def test_cycle_at_head():
    head = _make_cyclic([1, 2, 3, 4], 0)
    assert has_cycle(head) is True


def test_cycle_at_middle():
    head = _make_cyclic([1, 2, 3, 4, 5], 2)
    assert has_cycle(head) is True


def test_cycle_at_tail():
    head = _make_cyclic([1, 2, 3], 2)
    assert has_cycle(head) is True


# --- find_cycle_start ---

def test_start_no_cycle():
    assert find_cycle_start(_make_list([1, 2, 3])) is None


def test_start_cycle_at_head():
    head = _make_cyclic([1, 2, 3, 4], 0)
    assert find_cycle_start(head).val == 1


def test_start_cycle_at_middle():
    head = _make_cyclic([1, 2, 3, 4, 5], 2)
    assert find_cycle_start(head).val == 3


def test_start_self_loop():
    node = ListNode(42)
    node.next = node
    assert find_cycle_start(node).val == 42


# --- cycle_length ---

def test_length_no_cycle():
    assert cycle_length(_make_list([1, 2, 3])) == 0


def test_length_self_loop():
    node = ListNode(1)
    node.next = node
    assert cycle_length(node) == 1


def test_length_full_cycle():
    head = _make_cyclic([1, 2, 3, 4], 0)
    assert cycle_length(head) == 4


def test_length_partial_cycle():
    head = _make_cyclic([1, 2, 3, 4, 5], 2)
    assert cycle_length(head) == 3
