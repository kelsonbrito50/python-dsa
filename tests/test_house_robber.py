"""Tests for House Robber algorithms."""

import pytest
from src.dynamic_programming.house_robber import (
    house_robber,
    house_robber_ii,
    house_robber_memo,
)


class TestHouseRobber:
    def test_empty(self):
        assert house_robber([]) == 0

    def test_single(self):
        assert house_robber([5]) == 5

    def test_two_houses(self):
        assert house_robber([1, 2]) == 2

    def test_basic(self):
        assert house_robber([1, 2, 3, 1]) == 4

    def test_larger(self):
        assert house_robber([2, 7, 9, 3, 1]) == 12

    def test_all_same(self):
        assert house_robber([5, 5, 5, 5, 5]) == 15

    def test_decreasing(self):
        assert house_robber([10, 5, 3, 1]) == 13

    def test_alternating(self):
        assert house_robber([1, 100, 1, 100, 1]) == 200


class TestHouseRobberII:
    def test_empty(self):
        assert house_robber_ii([]) == 0

    def test_single(self):
        assert house_robber_ii([5]) == 5

    def test_two(self):
        assert house_robber_ii([1, 2]) == 2

    def test_circle(self):
        assert house_robber_ii([2, 3, 2]) == 3

    def test_circle_larger(self):
        assert house_robber_ii([1, 2, 3, 1]) == 4

    def test_circle_complex(self):
        assert house_robber_ii([1, 3, 1, 3, 100]) == 103


class TestHouseRobberMemo:
    def test_empty(self):
        assert house_robber_memo([]) == 0

    def test_basic(self):
        assert house_robber_memo([1, 2, 3, 1]) == 4

    def test_larger(self):
        assert house_robber_memo([2, 7, 9, 3, 1]) == 12

    def test_matches_iterative(self):
        nums = [4, 1, 2, 7, 5, 3, 1]
        assert house_robber_memo(nums) == house_robber(nums)
