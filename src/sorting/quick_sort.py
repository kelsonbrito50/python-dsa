"""
Quick Sort — Divide and conquer sorting.

Time:  O(n log n) average, O(n²) worst case
Space: O(log n) — recursive stack
"""


def quick_sort(arr: list[int]) -> list[int]:
    """Sort array using quick sort algorithm."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr: list[int], low: int = 0, high: int | None = None) -> None:
    """In-place quick sort using Lomuto partition."""
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_idx = _partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)


def _partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
