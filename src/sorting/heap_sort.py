"""
Heap Sort — In-place, comparison-based.

Time:  O(n log n)
Space: O(1)
"""


def heap_sort(arr: list[int]) -> list[int]:
    result = arr.copy()
    n = len(result)

    for i in range(n // 2 - 1, -1, -1):
        _heapify(result, n, i)

    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        _heapify(result, i, 0)

    return result


def _heapify(arr: list[int], n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)
