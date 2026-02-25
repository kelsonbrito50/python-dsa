"""
Level Order Traversal (BFS) of a Binary Tree.

Uses a queue to traverse the tree level by level (breadth-first).

Time:  O(n) — visits every node once
Space: O(n) — queue holds at most one level of nodes
"""

from collections import deque
from typing import Optional


class TreeNode:
    """Binary tree node."""

    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> list[list[int]]:
    """
    Return values grouped by level.

    >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    >>> level_order(root)
    [[3], [9, 20], [15, 7]]
    >>> level_order(None)
    []
    """
    if not root:
        return []

    result: list[list[int]] = []
    queue: deque[TreeNode] = deque([root])

    while queue:
        level_size = len(queue)
        level: list[int] = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


def max_depth(root: Optional[TreeNode]) -> int:
    """
    Return the maximum depth of a binary tree using BFS.

    >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    >>> max_depth(root)
    3
    >>> max_depth(None)
    0
    """
    if not root:
        return 0

    depth = 0
    queue: deque[TreeNode] = deque([root])

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return depth
