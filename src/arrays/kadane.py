"""
Kadane's Algorithm — Maximum subarray sum.

Time:  O(n)
Space: O(1)
"""


def max_subarray_sum(arr: list[int]) -> int:
    """Find the contiguous subarray with the largest sum."""
    if not arr:
        return 0

    max_sum = current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum
