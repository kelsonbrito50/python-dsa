"""
Binary Search — Find element in sorted array.

Time:  O(log n)
Space: O(1) iterative, O(log n) recursive
"""


def binary_search(arr: list[int], target: int) -> int:
    """Iterative binary search. Returns index or -1."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(
    arr: list[int], target: int, left: int = 0, right: int | None = None
) -> int:
    """Recursive binary search."""
    if right is None:
        right = len(arr) - 1

    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
