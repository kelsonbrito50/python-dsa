from src.strings.manipulation import is_anagram, reverse_words, first_unique_char, longest_common_prefix

def test_anagram():
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False

def test_reverse_words():
    assert reverse_words("the sky is blue") == "blue is sky the"

def test_first_unique():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("aabb") == -1

def test_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
