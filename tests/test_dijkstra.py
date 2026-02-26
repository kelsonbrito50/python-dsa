"""Tests for Dijkstra's shortest path algorithm."""

import pytest
from src.graphs.dijkstra import dijkstra, shortest_path


@pytest.fixture
def simple_graph():
    """
    A -> B (1) -> D (3)
    A -> C (4)
    B -> C (2)
    C -> D (1)
    """
    return {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 3)],
        "C": [("D", 1)],
        "D": [],
    }


class TestDijkstra:
    def test_distances(self, simple_graph):
        dist, _ = dijkstra(simple_graph, "A")
        assert dist["A"] == 0
        assert dist["B"] == 1
        assert dist["C"] == 3  # A->B->C
        assert dist["D"] == 4  # A->B->C->D

    def test_previous_pointers(self, simple_graph):
        _, prev = dijkstra(simple_graph, "A")
        assert prev["A"] is None
        assert prev["B"] == "A"
        assert prev["C"] == "B"
        assert prev["D"] in ("B", "C")  # both paths cost 4

    def test_unreachable_vertex(self):
        graph = {"A": [("B", 1)], "B": [], "C": []}
        dist, _ = dijkstra(graph, "A")
        assert dist["C"] == float("inf")

    def test_single_vertex(self):
        graph = {"X": []}
        dist, prev = dijkstra(graph, "X")
        assert dist["X"] == 0
        assert prev["X"] is None


class TestShortestPath:
    def test_path_reconstruction(self, simple_graph):
        cost, path = shortest_path(simple_graph, "A", "D")
        assert cost == 4
        assert path in (["A", "B", "C", "D"], ["A", "B", "D"])  # tie

    def test_direct_neighbour(self, simple_graph):
        cost, path = shortest_path(simple_graph, "A", "B")
        assert cost == 1
        assert path == ["A", "B"]

    def test_same_source_target(self, simple_graph):
        cost, path = shortest_path(simple_graph, "A", "A")
        assert cost == 0
        assert path == ["A"]

    def test_unreachable_returns_empty(self):
        graph = {"A": [], "B": []}
        cost, path = shortest_path(graph, "A", "B")
        assert cost == float("inf")
        assert path == []
