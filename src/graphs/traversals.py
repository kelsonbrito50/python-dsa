"""
Graph Traversals — BFS and DFS.

BFS: O(V + E) time, O(V) space — uses queue
DFS: O(V + E) time, O(V) space — uses stack/recursion
"""

from collections import deque


Graph = dict[str, list[str]]


def bfs(graph: Graph, start: str) -> list[str]:
    """Breadth-first search — level by level."""
    visited: set[str] = set()
    queue: deque[str] = deque([start])
    result: list[str] = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(n for n in graph.get(node, []) if n not in visited)

    return result


def dfs(graph: Graph, start: str) -> list[str]:
    """Depth-first search — iterative with stack."""
    visited: set[str] = set()
    stack: list[str] = [start]
    result: list[str] = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(reversed(graph.get(node, [])))

    return result


def dfs_recursive(
    graph: Graph, node: str, visited: set[str] | None = None
) -> list[str]:
    """Depth-first search — recursive."""
    if visited is None:
        visited = set()

    visited.add(node)
    result = [node]

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))

    return result
