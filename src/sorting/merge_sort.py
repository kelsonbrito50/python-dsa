"""
Merge Sort — Stable divide and conquer sorting.

Time:  O(n log n) — all cases
Space: O(n) — auxiliary arrays during merge
"""


def merge_sort(arr: list[int]) -> list[int]:
    """Sort array using merge sort algorithm (returns new list)."""
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return _merge(left, right)


def _merge(left: list[int], right: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def merge_sort_inplace(arr: list[int], left: int = 0, right: int | None = None) -> None:
    """In-place merge sort (still uses O(n) temp space during merge)."""
    if right is None:
        right = len(arr) - 1

    if left < right:
        mid = (left + right) // 2
        merge_sort_inplace(arr, left, mid)
        merge_sort_inplace(arr, mid + 1, right)
        _merge_inplace(arr, left, mid, right)


def _merge_inplace(arr: list[int], left: int, mid: int, right: int) -> None:
    """Merge two sorted subarrays arr[left..mid] and arr[mid+1..right]."""
    temp_left = arr[left:mid + 1]
    temp_right = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(temp_left) and j < len(temp_right):
        if temp_left[i] <= temp_right[j]:
            arr[k] = temp_left[i]
            i += 1
        else:
            arr[k] = temp_right[j]
            j += 1
        k += 1

    while i < len(temp_left):
        arr[k] = temp_left[i]
        i += 1
        k += 1

    while j < len(temp_right):
        arr[k] = temp_right[j]
        j += 1
        k += 1
