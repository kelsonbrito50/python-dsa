"""
Trie (Prefix Tree) — Classic string data structure.

A Trie stores strings character-by-character in a tree, enabling
O(m) insert/search/prefix operations where m = word length.

Common applications:
- Autocomplete / typeahead suggestions
- Spell checkers
- IP routing (longest prefix match)
- Word games (Boggle, Scrabble solvers)

LeetCode: 208 (Implement Trie), 211 (Search Word), 212 (Word Search II)
"""

from __future__ import annotations
from typing import List, Optional


class TrieNode:
    """Single node in the Trie."""

    __slots__ = ("children", "is_end", "count")

    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False
        self.count: int = 0  # words passing through this node


class Trie:
    """
    Prefix tree with insert, search, prefix query, delete,
    and autocomplete support.

    >>> t = Trie()
    >>> t.insert("apple")
    >>> t.search("apple")
    True
    >>> t.search("app")
    False
    >>> t.starts_with("app")
    True
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    # ── Core operations ────────────────────────────────────────

    def insert(self, word: str) -> None:
        """Insert a word into the trie. O(m)"""
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.count += 1
        node.is_end = True

    def search(self, word: str) -> bool:
        """Return True if the exact word exists. O(m)"""
        node = self._find_node(word)
        return node is not None and node.is_end

    def starts_with(self, prefix: str) -> bool:
        """Return True if any word starts with the given prefix. O(m)"""
        return self._find_node(prefix) is not None

    def delete(self, word: str) -> bool:
        """
        Remove a word from the trie. Returns True if it existed.
        Prunes nodes that are no longer part of any word.
        """
        return self._delete(self.root, word, 0)

    # ── Extended operations ────────────────────────────────────

    def count_prefix(self, prefix: str) -> int:
        """Count how many inserted words share this prefix."""
        node = self._find_node(prefix)
        return node.count if node else 0

    def autocomplete(self, prefix: str, limit: int = 10) -> List[str]:
        """
        Return up to `limit` words that start with `prefix`,
        in lexicographic order.
        """
        node = self._find_node(prefix)
        if node is None:
            return []
        results: List[str] = []
        self._dfs_collect(node, list(prefix), results, limit)
        return results

    def longest_common_prefix(self) -> str:
        """
        Find the longest prefix shared by ALL words in the trie.
        Returns "" if trie is empty or no common prefix exists.
        """
        node = self.root
        prefix: List[str] = []
        while len(node.children) == 1 and not node.is_end:
            ch, child = next(iter(node.children.items()))
            prefix.append(ch)
            node = child
        return "".join(prefix)

    # ── Wildcard search (LeetCode 211) ─────────────────────────

    def search_wildcard(self, pattern: str, wildcard: str = ".") -> bool:
        """
        Search with wildcard support. The wildcard character matches
        any single character (like LeetCode 211 — WordDictionary).
        """
        return self._wildcard(self.root, pattern, 0, wildcard)

    # ── Private helpers ────────────────────────────────────────

    def _find_node(self, prefix: str) -> Optional[TrieNode]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def _delete(self, node: TrieNode, word: str, depth: int) -> bool:
        if depth == len(word):
            if not node.is_end:
                return False
            node.is_end = False
            return True

        ch = word[depth]
        if ch not in node.children:
            return False

        child = node.children[ch]
        found = self._delete(child, word, depth + 1)

        if found:
            child.count -= 1
            if child.count == 0 and not child.is_end:
                del node.children[ch]

        return found

    def _dfs_collect(
        self,
        node: TrieNode,
        path: List[str],
        results: List[str],
        limit: int,
    ) -> None:
        if len(results) >= limit:
            return
        if node.is_end:
            results.append("".join(path))
        for ch in sorted(node.children):
            path.append(ch)
            self._dfs_collect(node.children[ch], path, results, limit)
            path.pop()

    def _wildcard(
        self, node: TrieNode, pattern: str, idx: int, wildcard: str
    ) -> bool:
        if idx == len(pattern):
            return node.is_end
        ch = pattern[idx]
        if ch == wildcard:
            return any(
                self._wildcard(child, pattern, idx + 1, wildcard)
                for child in node.children.values()
            )
        if ch not in node.children:
            return False
        return self._wildcard(node.children[ch], pattern, idx + 1, wildcard)
