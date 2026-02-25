"""
Stack — LIFO data structure.

Push/Pop/Peek: O(1)
"""


class Stack:
    def __init__(self) -> None:
        self._items: list[int] = []

    def push(self, val: int) -> None:
        self._items.append(val)

    def pop(self) -> int | None:
        return self._items.pop() if self._items else None

    def peek(self) -> int | None:
        return self._items[-1] if self._items else None

    def is_empty(self) -> bool:
        return len(self._items) == 0

    @property
    def size(self) -> int:
        return len(self._items)


def is_valid_parentheses(s: str) -> bool:
    """Check if string has valid parentheses. O(n) time, O(n) space."""
    stack: list[str] = []
    pairs = {"(": ")", "[": "]", "{": "}"}

    for char in s:
        if char in pairs:
            stack.append(pairs[char])
        elif not stack or stack.pop() != char:
            return False

    return len(stack) == 0
