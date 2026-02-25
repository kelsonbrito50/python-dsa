from src.backtracking.permutations import permutations, subsets

def test_permutations():
    result = permutations([1, 2, 3])
    assert len(result) == 6
    assert [1, 2, 3] in result

def test_subsets():
    result = subsets([1, 2])
    assert len(result) == 4
    assert [] in result
    assert [1, 2] in result
