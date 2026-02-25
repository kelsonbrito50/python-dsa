from src.sorting.heap_sort import heap_sort

def test_basic():
    assert heap_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]

def test_single():
    assert heap_sort([42]) == [42]
