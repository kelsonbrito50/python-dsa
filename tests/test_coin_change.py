from src.dynamic_programming.coin_change import coin_change


def test_basic():
    assert coin_change([1, 5, 10, 25], 30) == 2  # 25+5


def test_impossible():
    assert coin_change([2], 3) == -1


def test_zero():
    assert coin_change([1], 0) == 0


def test_single_coin():
    assert coin_change([1], 5) == 5


def test_multiple_ways():
    assert coin_change([1, 3, 4], 6) == 2  # 3+3
