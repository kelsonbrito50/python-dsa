from src.heaps.priority_queue import kth_largest, top_k_frequent, merge_k_sorted

def test_kth_largest():
    assert kth_largest([3, 2, 1, 5, 6, 4], 2) == 5

def test_top_k():
    assert set(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}

def test_merge_k():
    assert merge_k_sorted([[1, 4, 5], [1, 3, 4], [2, 6]]) == [1, 1, 2, 3, 4, 4, 5, 6]
