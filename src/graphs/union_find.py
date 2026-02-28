"""Union-Find (Disjoint Set Union) with path compression and union by rank.

Supports:
- find(x): returns the root representative of x's set
- union(x, y): merges the sets containing x and y
- connected(x, y): checks if x and y are in the same set
- components: returns the current number of disjoint sets

Time complexity: nearly O(1) amortized per operation (inverse Ackermann).
"""


class UnionFind:
    """Weighted Quick-Union with path compression."""

    def __init__(self, n: int) -> None:
        """Initialise *n* elements (0 … n-1), each in its own set."""
        self.parent = list(range(n))
        self.rank = [0] * n
        self._components = n

    # ------------------------------------------------------------------
    # Core operations
    # ------------------------------------------------------------------

    def find(self, x: int) -> int:
        """Return root representative with full path compression."""
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path halving
            x = self.parent[x]
        return x

    def union(self, x: int, y: int) -> bool:
        """Merge sets of *x* and *y*. Returns True if a merge happened."""
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        self._components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check whether *x* and *y* belong to the same set."""
        return self.find(x) == self.find(y)

    @property
    def components(self) -> int:
        """Return the number of disjoint sets."""
        return self._components


# ------------------------------------------------------------------
# Classic application: detect cycle in an undirected graph
# ------------------------------------------------------------------

def has_cycle(n: int, edges: list[tuple[int, int]]) -> bool:
    """Return True if the undirected graph (n vertices, edge list) has a cycle."""
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return True
    return False
