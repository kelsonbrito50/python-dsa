"""
Sliding Window — Find max sum subarray of size k.

Time:  O(n)
Space: O(1)
"""


def max_sum_subarray(arr: list[int], k: int) -> int:
    """Find maximum sum of any contiguous subarray of size k."""
    if len(arr) < k:
        return 0

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def longest_unique_substring(s: str) -> int:
    """Length of longest substring without repeating characters. O(n)."""
    seen: dict[str, int] = {}
    start = 0
    max_len = 0

    for end, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1
        seen[char] = end
        max_len = max(max_len, end - start + 1)

    return max_len
