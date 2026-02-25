from src.searching.binary_search import binary_search, binary_search_recursive


def test_binary_search_found():
    assert binary_search([1, 3, 5, 7, 9], 5) == 2


def test_binary_search_not_found():
    assert binary_search([1, 3, 5, 7, 9], 4) == -1


def test_recursive():
    assert binary_search_recursive([1, 3, 5, 7, 9], 7) == 3
