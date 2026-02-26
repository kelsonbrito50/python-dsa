"""
Dijkstra's Shortest Path Algorithm

Finds the shortest path from a source vertex to all other vertices
in a weighted graph with non-negative edge weights.

Time Complexity: O((V + E) log V) with a min-heap
Space Complexity: O(V)
"""

import heapq
from typing import Dict, List, Tuple


def dijkstra(
    graph: Dict[str, List[Tuple[str, float]]], source: str
) -> Tuple[Dict[str, float], Dict[str, str | None]]:
    """
    Compute shortest distances from source to all reachable vertices.

    Args:
        graph: Adjacency list where graph[u] = [(v, weight), ...].
               Every vertex that appears as a neighbour must also be a key
               (even if its list is empty).
        source: Starting vertex.

    Returns:
        distances: {vertex: shortest_distance} (unreachable → float('inf'))
        previous:  {vertex: predecessor} for path reconstruction (source → None)
    """
    distances: Dict[str, float] = {v: float("inf") for v in graph}
    previous: Dict[str, str | None] = {v: None for v in graph}
    distances[source] = 0.0

    # Min-heap: (distance, vertex)
    heap: List[Tuple[float, str]] = [(0.0, source)]

    while heap:
        dist_u, u = heapq.heappop(heap)

        # Skip stale entries
        if dist_u > distances[u]:
            continue

        for v, weight in graph[u]:
            alt = dist_u + weight
            if alt < distances[v]:
                distances[v] = alt
                previous[v] = u
                heapq.heappush(heap, (alt, v))

    return distances, previous


def shortest_path(
    graph: Dict[str, List[Tuple[str, float]]], source: str, target: str
) -> Tuple[float, List[str]]:
    """
    Return the shortest distance and path from source to target.

    Returns:
        (distance, path) where path is a list of vertices from source to target.
        If unreachable, returns (float('inf'), []).
    """
    distances, previous = dijkstra(graph, source)

    if distances[target] == float("inf"):
        return float("inf"), []

    path: List[str] = []
    current: str | None = target
    while current is not None:
        path.append(current)
        current = previous[current]

    return distances[target], list(reversed(path))
