"""
Reverse a Linked List — Iterative and Recursive approaches.

Iterative: O(n) time, O(1) space
Recursive: O(n) time, O(n) space (call stack)

LeetCode 206 — Reverse Linked List
"""
from __future__ import annotations

from src.linked_lists.singly import Node


def reverse_iterative(head: Node | None) -> Node | None:
    """Reverse list iteratively — O(n) time, O(1) space."""
    prev, current = None, head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev


def reverse_recursive(head: Node | None) -> Node | None:
    """Reverse list recursively — O(n) time, O(n) space."""
    if not head or not head.next:
        return head
    new_head = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return new_head


def reverse_between(head: Node | None, left: int, right: int) -> Node | None:
    """Reverse nodes between positions left and right (1-indexed).

    LeetCode 92 — Reverse Linked List II.
    O(n) time, O(1) space.
    """
    if not head or left == right:
        return head

    dummy = Node(0, head)
    prev = dummy
    for _ in range(left - 1):
        if prev.next is None:
            return head
        prev = prev.next

    current = prev.next
    for _ in range(right - left):
        if current is None or current.next is None:
            break
        nxt = current.next
        current.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt

    return dummy.next


def _to_list(head: Node | None) -> list[int]:
    """Helper: convert linked list to Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def _from_list(vals: list[int]) -> Node | None:
    """Helper: create linked list from Python list."""
    if not vals:
        return None
    head = Node(vals[0])
    current = head
    for v in vals[1:]:
        current.next = Node(v)
        current = current.next
    return head
