from src.matrix.operations import rotate_90, spiral_order

def test_rotate():
    m = [[1, 2], [3, 4]]
    rotate_90(m)
    assert m == [[3, 1], [4, 2]]

def test_spiral():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert spiral_order(m) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
