from src.sorting.quick_sort import quick_sort, quick_sort_inplace


def test_quick_sort():
    assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_quick_sort_empty():
    assert quick_sort([]) == []


def test_quick_sort_inplace():
    arr = [5, 3, 8, 1, 2]
    quick_sort_inplace(arr)
    assert arr == [1, 2, 3, 5, 8]
