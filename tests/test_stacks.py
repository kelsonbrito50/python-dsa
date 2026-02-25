from src.stacks.stack import Stack, is_valid_parentheses

def test_push_pop():
    s = Stack()
    s.push(1)
    s.push(2)
    assert s.pop() == 2
    assert s.pop() == 1

def test_valid_parentheses():
    assert is_valid_parentheses("()[]{}") is True
    assert is_valid_parentheses("(]") is False
    assert is_valid_parentheses("{[()]}") is True
    assert is_valid_parentheses("((") is False
