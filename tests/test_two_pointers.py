from src.arrays.two_pointers import two_sum_sorted, remove_duplicates, is_palindrome

def test_two_sum_sorted():
    assert two_sum_sorted([2, 7, 11, 15], 9) == (0, 1)
    assert two_sum_sorted([1, 3, 5, 7], 12) == (2, 3)

def test_remove_duplicates():
    nums = [1, 1, 2, 3, 3]
    assert remove_duplicates(nums) == 3

def test_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("hello") is False
