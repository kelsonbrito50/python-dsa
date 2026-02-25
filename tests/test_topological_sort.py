"""Tests for topological sort algorithms."""

import pytest
from src.graphs.topological_sort import (
    topological_sort_kahn,
    topological_sort_dfs,
    all_topological_sorts,
    course_schedule,
)


def is_valid_topological_order(num_nodes, edges, order):
    """Helper: verify that order respects all edge constraints."""
    if len(order) != num_nodes:
        return False
    position = {node: i for i, node in enumerate(order)}
    return all(position[u] < position[v] for u, v in edges)


class TestKahn:
    def test_simple_dag(self):
        # 0 → 1 → 2
        result = topological_sort_kahn(3, [(0, 1), (1, 2)])
        assert is_valid_topological_order(3, [(0, 1), (1, 2)], result)

    def test_diamond_dag(self):
        # 0 → 1, 0 → 2, 1 → 3, 2 → 3
        edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
        result = topological_sort_kahn(4, edges)
        assert is_valid_topological_order(4, edges, result)

    def test_no_edges(self):
        result = topological_sort_kahn(3, [])
        assert sorted(result) == [0, 1, 2]

    def test_single_node(self):
        assert topological_sort_kahn(1, []) == [0]

    def test_cycle_detection(self):
        assert topological_sort_kahn(3, [(0, 1), (1, 2), (2, 0)]) == []

    def test_self_loop(self):
        assert topological_sort_kahn(2, [(0, 0)]) == []

    def test_complex_dag(self):
        # 6 nodes, multiple paths
        edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
        result = topological_sort_kahn(6, edges)
        assert is_valid_topological_order(6, edges, result)


class TestDFS:
    def test_simple_dag(self):
        result = topological_sort_dfs(3, [(0, 1), (1, 2)])
        assert is_valid_topological_order(3, [(0, 1), (1, 2)], result)

    def test_diamond_dag(self):
        edges = [(0, 1), (0, 2), (1, 3), (2, 3)]
        result = topological_sort_dfs(4, edges)
        assert is_valid_topological_order(4, edges, result)

    def test_no_edges(self):
        result = topological_sort_dfs(3, [])
        assert sorted(result) == [0, 1, 2]

    def test_cycle_detection(self):
        assert topological_sort_dfs(3, [(0, 1), (1, 2), (2, 0)]) == []

    def test_complex_dag(self):
        edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
        result = topological_sort_dfs(6, edges)
        assert is_valid_topological_order(6, edges, result)


class TestAllTopologicalSorts:
    def test_linear(self):
        # Only one valid order: 0 → 1 → 2
        result = all_topological_sorts(3, [(0, 1), (1, 2)])
        assert result == [[0, 1, 2]]

    def test_parallel(self):
        # 0 → 2, 1 → 2: valid orders are [0,1,2] and [1,0,2]
        result = all_topological_sorts(3, [(0, 2), (1, 2)])
        assert len(result) == 2
        for order in result:
            assert is_valid_topological_order(3, [(0, 2), (1, 2)], order)

    def test_no_edges(self):
        # 3 nodes, no edges: 3! = 6 permutations
        result = all_topological_sorts(3, [])
        assert len(result) == 6


class TestCourseSchedule:
    def test_basic(self):
        # To take 1, first take 0
        result = course_schedule(2, [[1, 0]])
        assert result == [0, 1]

    def test_multiple_prereqs(self):
        result = course_schedule(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
        assert is_valid_topological_order(4, [(0, 1), (0, 2), (1, 3), (2, 3)], result)

    def test_impossible(self):
        assert course_schedule(2, [[1, 0], [0, 1]]) == []

    def test_no_prereqs(self):
        result = course_schedule(3, [])
        assert sorted(result) == [0, 1, 2]
