"""
House Robber Problem

Given a list of non-negative integers representing money in each house,
determine the maximum amount you can rob without robbing two adjacent houses.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def house_robber(nums: list[int]) -> int:
    """Return max money robbing non-adjacent houses."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2 = 0  # two houses back
    prev1 = 0  # one house back

    for num in nums:
        current = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = current

    return prev1


def house_robber_ii(nums: list[int]) -> int:
    """House Robber II - houses arranged in a circle."""
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums)

    # Rob houses 0..n-2 or 1..n-1 (can't rob both first and last)
    return max(house_robber(nums[:-1]), house_robber(nums[1:]))


def house_robber_memo(nums: list[int]) -> int:
    """Memoized recursive approach for comparison."""
    memo = {}

    def rob(i: int) -> int:
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]
        memo[i] = max(rob(i + 1), nums[i] + rob(i + 2))
        return memo[i]

    return rob(0)
