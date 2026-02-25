"""
Two Sum — Find two numbers that add up to target.

Time:  O(n) — single pass with hash map
Space: O(n) — storing seen values
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """Return indices of two numbers that add up to target."""
    seen: dict[int, int] = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """Two-pointer approach for sorted arrays. O(n) time, O(1) space."""
    left, right = 0, len(nums) - 1

    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        elif total < target:
            left += 1
        else:
            right -= 1

    return []
