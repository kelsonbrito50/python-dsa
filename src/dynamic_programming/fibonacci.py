"""
Fibonacci — Classic DP problem.

Recursive: O(2^n) — DON'T
Memoized: O(n) time, O(n) space
Bottom-up: O(n) time, O(1) space ← optimal
"""


def fibonacci_memo(n: int, memo: dict[int, int] | None = None) -> int:
    """Top-down with memoization. O(n) time, O(n) space."""
    if memo is None:
        memo = {}
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]


def fibonacci_dp(n: int) -> int:
    """Bottom-up DP. O(n) time, O(1) space."""
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr


def climbing_stairs(n: int) -> int:
    """Number of ways to climb n stairs (1 or 2 steps). O(n) time, O(1) space."""
    if n <= 2:
        return n
    prev, curr = 1, 2
    for _ in range(3, n + 1):
        prev, curr = curr, prev + curr
    return curr
