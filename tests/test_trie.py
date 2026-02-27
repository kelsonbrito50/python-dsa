"""Tests for Trie (Prefix Tree) implementation."""

import pytest
from src.tries.trie import Trie


# ── Basic insert / search ──────────────────────────────────────

class TestTrieBasic:
    def test_search_existing_word(self):
        t = Trie()
        t.insert("apple")
        assert t.search("apple") is True

    def test_search_missing_word(self):
        t = Trie()
        t.insert("apple")
        assert t.search("app") is False

    def test_search_empty_trie(self):
        assert Trie().search("hello") is False

    def test_insert_empty_string(self):
        t = Trie()
        t.insert("")
        assert t.search("") is True
        assert t.starts_with("") is True

    def test_multiple_inserts(self):
        t = Trie()
        words = ["apple", "app", "apt", "bat", "ball", "banana"]
        for w in words:
            t.insert(w)
        for w in words:
            assert t.search(w) is True
        assert t.search("ap") is False
        assert t.search("ban") is False


# ── Prefix queries ─────────────────────────────────────────────

class TestTriePrefix:
    def test_starts_with(self):
        t = Trie()
        t.insert("apple")
        assert t.starts_with("app") is True
        assert t.starts_with("apple") is True
        assert t.starts_with("b") is False

    def test_count_prefix(self):
        t = Trie()
        for w in ["apple", "app", "application", "bat"]:
            t.insert(w)
        assert t.count_prefix("app") == 3
        assert t.count_prefix("apple") == 1  # only "apple" not "application"
        assert t.count_prefix("bat") == 1
        assert t.count_prefix("xyz") == 0


# ── Delete ─────────────────────────────────────────────────────

class TestTrieDelete:
    def test_delete_existing(self):
        t = Trie()
        t.insert("apple")
        assert t.delete("apple") is True
        assert t.search("apple") is False

    def test_delete_missing(self):
        t = Trie()
        t.insert("apple")
        assert t.delete("app") is False

    def test_delete_preserves_prefix_sibling(self):
        t = Trie()
        t.insert("apple")
        t.insert("app")
        t.delete("apple")
        assert t.search("app") is True
        assert t.search("apple") is False

    def test_delete_preserves_longer_word(self):
        t = Trie()
        t.insert("app")
        t.insert("apple")
        t.delete("app")
        assert t.search("apple") is True
        assert t.search("app") is False


# ── Autocomplete ───────────────────────────────────────────────

class TestAutocomplete:
    def test_basic_autocomplete(self):
        t = Trie()
        for w in ["apple", "app", "application", "bat"]:
            t.insert(w)
        result = t.autocomplete("app")
        assert result == ["app", "apple", "application"]

    def test_autocomplete_limit(self):
        t = Trie()
        for w in ["a", "ab", "abc", "abcd", "abcde"]:
            t.insert(w)
        assert len(t.autocomplete("a", limit=3)) == 3

    def test_autocomplete_no_match(self):
        t = Trie()
        t.insert("hello")
        assert t.autocomplete("xyz") == []


# ── Longest common prefix ─────────────────────────────────────

class TestLongestCommonPrefix:
    def test_common_prefix(self):
        t = Trie()
        for w in ["flower", "flow", "flight"]:
            t.insert(w)
        assert t.longest_common_prefix() == "fl"

    def test_no_common_prefix(self):
        t = Trie()
        for w in ["dog", "cat", "rat"]:
            t.insert(w)
        assert t.longest_common_prefix() == ""

    def test_all_same(self):
        t = Trie()
        t.insert("aaa")
        assert t.longest_common_prefix() == "aaa"


# ── Wildcard search ────────────────────────────────────────────

class TestWildcard:
    def test_wildcard_match(self):
        t = Trie()
        t.insert("bad")
        t.insert("dad")
        t.insert("mad")
        assert t.search_wildcard(".ad") is True
        assert t.search_wildcard("b..") is True
        assert t.search_wildcard("b.d") is True

    def test_wildcard_no_match(self):
        t = Trie()
        t.insert("bad")
        assert t.search_wildcard("..") is False
        assert t.search_wildcard("b.de") is False

    def test_no_wildcard_exact(self):
        t = Trie()
        t.insert("hello")
        assert t.search_wildcard("hello") is True
        assert t.search_wildcard("hell") is False
