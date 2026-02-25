"""
Two Pointers — Efficient array traversal.

Time: O(n) — single pass
Space: O(1) — in-place
"""


def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int]:
    """Find two indices in SORTED array that sum to target. O(n)."""
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return (left, right)
        elif total < target:
            left += 1
        else:
            right -= 1
    return (-1, -1)


def remove_duplicates(nums: list[int]) -> int:
    """Remove duplicates in-place from sorted array. Returns new length. O(n)."""
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write


def is_palindrome(s: str) -> bool:
    """Check if string is palindrome (ignoring non-alphanumeric). O(n)."""
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True
