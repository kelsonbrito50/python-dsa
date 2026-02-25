"""Tests for reverse linked list algorithms."""
import pytest

from src.linked_lists.reverse_linked import (
    _from_list,
    _to_list,
    reverse_between,
    reverse_iterative,
    reverse_recursive,
)


class TestReverseIterative:
    def test_normal(self):
        head = _from_list([1, 2, 3, 4, 5])
        assert _to_list(reverse_iterative(head)) == [5, 4, 3, 2, 1]

    def test_two_nodes(self):
        head = _from_list([1, 2])
        assert _to_list(reverse_iterative(head)) == [2, 1]

    def test_single(self):
        head = _from_list([42])
        assert _to_list(reverse_iterative(head)) == [42]

    def test_empty(self):
        assert reverse_iterative(None) is None


class TestReverseRecursive:
    def test_normal(self):
        head = _from_list([1, 2, 3, 4, 5])
        assert _to_list(reverse_recursive(head)) == [5, 4, 3, 2, 1]

    def test_two_nodes(self):
        head = _from_list([1, 2])
        assert _to_list(reverse_recursive(head)) == [2, 1]

    def test_single(self):
        head = _from_list([42])
        assert _to_list(reverse_recursive(head)) == [42]

    def test_empty(self):
        assert reverse_recursive(None) is None


class TestReverseBetween:
    def test_middle(self):
        head = _from_list([1, 2, 3, 4, 5])
        assert _to_list(reverse_between(head, 2, 4)) == [1, 4, 3, 2, 5]

    def test_full(self):
        head = _from_list([1, 2, 3])
        assert _to_list(reverse_between(head, 1, 3)) == [3, 2, 1]

    def test_same_position(self):
        head = _from_list([1, 2, 3])
        assert _to_list(reverse_between(head, 2, 2)) == [1, 2, 3]

    def test_single_node(self):
        head = _from_list([5])
        assert _to_list(reverse_between(head, 1, 1)) == [5]

    def test_empty(self):
        assert reverse_between(None, 1, 1) is None
