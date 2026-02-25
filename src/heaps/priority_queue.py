"""
Heap / Priority Queue — Top K problems.

Kth Largest: O(n log k)
Merge K Sorted: O(n log k)
"""

import heapq


def kth_largest(nums: list[int], k: int) -> int:
    """Find kth largest element. O(n log k) using min-heap."""
    return heapq.nlargest(k, nums)[-1]


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """Find k most frequent elements. O(n log k)."""
    from collections import Counter
    count = Counter(nums)
    return [x for x, _ in count.most_common(k)]


def merge_k_sorted(lists: list[list[int]]) -> list[int]:
    """Merge k sorted lists. O(n log k)."""
    result: list[int] = []
    heap: list[tuple[int, int, int]] = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))

    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result
