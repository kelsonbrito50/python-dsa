"""
Linked List Cycle Detection — Floyd's Tortoise and Hare Algorithm

Detect if a singly linked list contains a cycle, find the cycle start node,
and compute the cycle length.

Time:  O(n) for all operations
Space: O(1) — no extra data structures
"""


class ListNode:
    """Minimal singly linked list node."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    """Return True if the linked list has a cycle."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def find_cycle_start(head: ListNode | None) -> ListNode | None:
    """Return the node where the cycle begins, or None if no cycle."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            # Phase 2: find entry point
            entry = head
            while entry is not slow:
                entry = entry.next
                slow = slow.next
            return entry
    return None


def cycle_length(head: ListNode | None) -> int:
    """Return the length of the cycle, or 0 if no cycle."""
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            length = 1
            runner = slow.next
            while runner is not slow:
                length += 1
                runner = runner.next
            return length
    return 0
