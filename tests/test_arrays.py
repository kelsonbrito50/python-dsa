from src.arrays.two_sum import two_sum, two_sum_sorted


def test_two_sum_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_no_solution():
    assert two_sum([1, 2, 3], 10) == []


def test_two_sum_sorted():
    assert two_sum_sorted([1, 2, 3, 4, 5], 9) == [3, 4]
