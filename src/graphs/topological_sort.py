"""
Topological Sort — ordering vertices in a DAG such that for every
directed edge u→v, u comes before v.

Two classic approaches:
1. Kahn's Algorithm (BFS with in-degree tracking)
2. DFS-based (post-order reversal)

Applications: build systems, task scheduling, dependency resolution,
course prerequisites, package managers.

Time: O(V + E)
Space: O(V + E)
"""

from collections import deque, defaultdict


def topological_sort_kahn(num_nodes: int, edges: list[tuple[int, int]]) -> list[int]:
    """
    Kahn's algorithm using BFS and in-degree counting.
    Returns topological order, or empty list if cycle detected.

    Args:
        num_nodes: number of vertices (0 to num_nodes-1)
        edges: list of (u, v) meaning u must come before v
    """
    graph = defaultdict(list)
    in_degree = [0] * num_nodes

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    queue = deque([i for i in range(num_nodes) if in_degree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # If not all nodes processed, there's a cycle
    return result if len(result) == num_nodes else []


def topological_sort_dfs(num_nodes: int, edges: list[tuple[int, int]]) -> list[int]:
    """
    DFS-based topological sort using post-order reversal.
    Returns topological order, or empty list if cycle detected.
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    # States: 0 = unvisited, 1 = in progress, 2 = completed
    state = [0] * num_nodes
    result = []
    has_cycle = False

    def dfs(node: int) -> None:
        nonlocal has_cycle
        if has_cycle:
            return

        state[node] = 1  # Mark in progress

        for neighbor in graph[node]:
            if state[neighbor] == 1:  # Back edge = cycle
                has_cycle = True
                return
            if state[neighbor] == 0:
                dfs(neighbor)

        state[node] = 2  # Mark completed
        result.append(node)

    for i in range(num_nodes):
        if state[i] == 0:
            dfs(i)

    if has_cycle:
        return []

    result.reverse()
    return result


def all_topological_sorts(num_nodes: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    """
    Find ALL valid topological orderings using backtracking.
    Useful for understanding flexibility in scheduling.

    Warning: Can be exponential — use only for small graphs.
    """
    graph = defaultdict(list)
    in_degree = [0] * num_nodes

    for u, v in edges:
        graph[u].append(v)
        in_degree[v] += 1

    results = []
    current = []
    visited = [False] * num_nodes

    def backtrack():
        for i in range(num_nodes):
            if not visited[i] and in_degree[i] == 0:
                # Choose node i
                visited[i] = True
                current.append(i)
                for neighbor in graph[i]:
                    in_degree[neighbor] -= 1

                backtrack()

                # Undo choice
                visited[i] = False
                current.pop()
                for neighbor in graph[i]:
                    in_degree[neighbor] += 1

        if len(current) == num_nodes:
            results.append(current[:])

    backtrack()
    return results


def course_schedule(num_courses: int, prerequisites: list[list[int]]) -> list[int]:
    """
    LeetCode 210 — Course Schedule II.
    Given prerequisites[i] = [a, b] meaning "to take a, you must first take b",
    return the ordering of courses, or empty if impossible.
    """
    edges = [(b, a) for a, b in prerequisites]
    return topological_sort_kahn(num_courses, edges)
