from src.arrays.sliding_window import max_sum_subarray, longest_unique_substring

def test_max_sum():
    assert max_sum_subarray([1, 4, 2, 10, 23, 3, 1, 0, 20], 4) == 39

def test_longest_unique():
    assert longest_unique_substring("abcabcbb") == 3
    assert longest_unique_substring("bbbbb") == 1
    assert longest_unique_substring("pwwkew") == 3
