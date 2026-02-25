"""Tests for Longest Increasing Subsequence."""

from src.dynamic_programming.longest_increasing import (
    lis_dp,
    lis_binary_search,
    lis_with_sequence,
)


class TestLISDp:
    def test_basic(self):
        assert lis_dp([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_increasing(self):
        assert lis_dp([1, 2, 3, 4, 5]) == 5

    def test_decreasing(self):
        assert lis_dp([5, 4, 3, 2, 1]) == 1

    def test_single(self):
        assert lis_dp([42]) == 1

    def test_empty(self):
        assert lis_dp([]) == 0

    def test_duplicates(self):
        assert lis_dp([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6

    def test_all_same(self):
        assert lis_dp([7, 7, 7, 7]) == 1


class TestLISBinarySearch:
    def test_basic(self):
        assert lis_binary_search([10, 9, 2, 5, 3, 7, 101, 18]) == 4

    def test_increasing(self):
        assert lis_binary_search([1, 2, 3, 4, 5]) == 5

    def test_decreasing(self):
        assert lis_binary_search([5, 4, 3, 2, 1]) == 1

    def test_single(self):
        assert lis_binary_search([42]) == 1

    def test_empty(self):
        assert lis_binary_search([]) == 0

    def test_duplicates(self):
        assert lis_binary_search([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6

    def test_all_same(self):
        assert lis_binary_search([7, 7, 7, 7]) == 1


class TestLISWithSequence:
    def test_basic(self):
        result = lis_with_sequence([10, 9, 2, 5, 3, 7, 101, 18])
        assert len(result) == 4
        assert result == sorted(result)
        assert all(result[i] < result[i + 1] for i in range(len(result) - 1))

    def test_increasing(self):
        assert lis_with_sequence([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_empty(self):
        assert lis_with_sequence([]) == []

    def test_single(self):
        assert lis_with_sequence([42]) == [42]
