from src.graphs.traversals import bfs, dfs, dfs_recursive

GRAPH = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": [], "E": []}

def test_bfs():
    assert bfs(GRAPH, "A") == ["A", "B", "C", "D", "E"]

def test_dfs():
    result = dfs(GRAPH, "A")
    assert result[0] == "A"
    assert set(result) == {"A", "B", "C", "D", "E"}

def test_dfs_recursive():
    result = dfs_recursive(GRAPH, "A")
    assert result[0] == "A"
    assert set(result) == {"A", "B", "C", "D", "E"}
