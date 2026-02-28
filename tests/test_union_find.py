"""Tests for Union-Find (Disjoint Set Union)."""
import pytest
from src.graphs.union_find import UnionFind, has_cycle


class TestUnionFind:
    def test_initial_state(self):
        uf = UnionFind(5)
        assert uf.components == 5
        for i in range(5):
            assert uf.find(i) == i

    def test_union_and_connected(self):
        uf = UnionFind(6)
        assert uf.union(0, 1) is True
        assert uf.connected(0, 1)
        assert not uf.connected(0, 2)
        assert uf.components == 5

    def test_union_already_connected(self):
        uf = UnionFind(4)
        uf.union(0, 1)
        assert uf.union(0, 1) is False  # no merge
        assert uf.components == 3

    def test_transitive_connectivity(self):
        uf = UnionFind(5)
        uf.union(0, 1)
        uf.union(1, 2)
        uf.union(3, 4)
        assert uf.connected(0, 2)
        assert not uf.connected(2, 3)
        uf.union(2, 3)
        assert uf.connected(0, 4)
        assert uf.components == 1

    def test_single_element(self):
        uf = UnionFind(1)
        assert uf.find(0) == 0
        assert uf.components == 1


class TestHasCycle:
    def test_no_cycle(self):
        # Tree: 0-1, 1-2, 2-3
        assert has_cycle(4, [(0, 1), (1, 2), (2, 3)]) is False

    def test_with_cycle(self):
        # Triangle: 0-1, 1-2, 2-0
        assert has_cycle(3, [(0, 1), (1, 2), (2, 0)]) is True

    def test_empty_graph(self):
        assert has_cycle(5, []) is False

    def test_single_edge(self):
        assert has_cycle(2, [(0, 1)]) is False
