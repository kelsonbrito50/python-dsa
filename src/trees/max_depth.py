"""Maximum Depth of Binary Tree (LeetCode #104)

Time: O(n) — visit every node once
Space: O(h) — recursion stack, h = height of tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: Optional[TreeNode]) -> int:
    """Return the maximum depth of a binary tree.

    Depth = number of nodes along the longest path from root to leaf.
    """
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def max_depth_iterative(root: Optional[TreeNode]) -> int:
    """Iterative BFS approach using level-order traversal."""
    if root is None:
        return 0

    from collections import deque

    queue = deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth
