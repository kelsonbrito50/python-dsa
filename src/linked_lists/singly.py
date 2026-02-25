"""
Singly Linked List — Core operations.

Insert: O(1) head, O(n) tail
Search: O(n)
Delete: O(n)
"""


class Node:
    def __init__(self, val: int, next_node: "Node | None" = None):
        self.val = val
        self.next = next_node


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.size: int = 0

    def push(self, val: int) -> None:
        """Insert at head — O(1)."""
        self.head = Node(val, self.head)
        self.size += 1

    def pop(self) -> int | None:
        """Remove from head — O(1)."""
        if not self.head:
            return None
        val = self.head.val
        self.head = self.head.next
        self.size -= 1
        return val

    def find(self, val: int) -> bool:
        """Search for value — O(n)."""
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        return False

    def reverse(self) -> None:
        """Reverse the list in-place — O(n) time, O(1) space."""
        prev, current = None, self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def to_list(self) -> list[int]:
        """Convert to Python list for testing."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
