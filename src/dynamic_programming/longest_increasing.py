"""
Longest Increasing Subsequence (LIS)

Find the length of the longest strictly increasing subsequence.
Two approaches: O(n^2) DP and O(n log n) binary search.

Time:  O(n log n) optimal, O(n^2) basic DP
Space: O(n)
"""

from bisect import bisect_left


def lis_dp(nums: list[int]) -> int:
    """O(n^2) dynamic programming approach."""
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


def lis_binary_search(nums: list[int]) -> int:
    """O(n log n) patience sorting / binary search approach."""
    if not nums:
        return 0

    tails = []

    for num in nums:
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


def lis_with_sequence(nums: list[int]) -> list[int]:
    """Return the actual longest increasing subsequence (not just length)."""
    if not nums:
        return []

    n = len(nums)
    tails = []
    indices = []
    parent = [-1] * n

    for i, num in enumerate(nums):
        pos = bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
            indices.append(i)
        else:
            tails[pos] = num
            indices[pos] = i

        if pos > 0:
            parent[i] = indices[pos - 1]

    # Reconstruct
    result = []
    idx = indices[len(tails) - 1]
    while idx != -1:
        result.append(nums[idx])
        idx = parent[idx]

    return result[::-1]
