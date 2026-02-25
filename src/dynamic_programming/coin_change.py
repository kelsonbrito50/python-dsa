"""
Coin Change — Minimum coins to make amount.

Time:  O(amount * len(coins))
Space: O(amount)

Classic DP problem. Build up from 0 to target amount.
"""


def coin_change(coins: list[int], amount: int) -> int:
    """Return minimum coins needed, or -1 if impossible."""
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1

    return dp[amount] if dp[amount] != float("inf") else -1
