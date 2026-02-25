"""
Queue — FIFO data structure.

Enqueue/Dequeue: O(1) with deque
"""

from collections import deque


class Queue:
    def __init__(self) -> None:
        self._items: deque[int] = deque()

    def enqueue(self, val: int) -> None:
        self._items.append(val)

    def dequeue(self) -> int | None:
        return self._items.popleft() if self._items else None

    def peek(self) -> int | None:
        return self._items[0] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    @property
    def size(self) -> int:
        return len(self._items)
