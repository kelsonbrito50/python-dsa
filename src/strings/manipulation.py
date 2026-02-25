"""
String Problems — Common interview patterns.

Anagram: O(n) with counter
Reverse Words: O(n)
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    """Check if two strings are anagrams. O(n)."""
    return Counter(s) == Counter(t)


def reverse_words(s: str) -> str:
    """Reverse words in a string. O(n)."""
    return " ".join(s.split()[::-1])


def first_unique_char(s: str) -> int:
    """Find index of first non-repeating character. O(n)."""
    count = Counter(s)
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    return -1


def longest_common_prefix(strs: list[str]) -> str:
    """Find longest common prefix. O(n*m)."""
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
