"""
Backtracking — Permutations and Subsets.

Permutations: O(n!) time
Subsets: O(2^n) time
"""


def permutations(nums: list[int]) -> list[list[int]]:
    """Generate all permutations. O(n!)."""
    result: list[list[int]] = []

    def backtrack(path: list[int], remaining: list[int]) -> None:
        if not remaining:
            result.append(path[:])
            return
        for i in range(len(remaining)):
            path.append(remaining[i])
            backtrack(path, remaining[:i] + remaining[i + 1:])
            path.pop()

    backtrack([], nums)
    return result


def subsets(nums: list[int]) -> list[list[int]]:
    """Generate all subsets (power set). O(2^n)."""
    result: list[list[int]] = []

    def backtrack(start: int, path: list[int]) -> None:
        result.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
