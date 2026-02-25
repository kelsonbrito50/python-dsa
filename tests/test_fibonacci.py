from src.dynamic_programming.fibonacci import fibonacci_memo, fibonacci_dp, climbing_stairs

def test_fib_memo():
    assert fibonacci_memo(10) == 55
    assert fibonacci_memo(0) == 0
    assert fibonacci_memo(1) == 1

def test_fib_dp():
    assert fibonacci_dp(10) == 55
    assert fibonacci_dp(20) == 6765

def test_climbing_stairs():
    assert climbing_stairs(3) == 3
    assert climbing_stairs(5) == 8
