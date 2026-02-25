"""Validate Binary Search Tree (LeetCode #98)

Time: O(n) — visit every node once
Space: O(h) — recursion stack
"""

from typing import Optional
import math


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Check if a binary tree is a valid BST using range validation."""

    def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
        if node is None:
            return True
        if node.val <= low or node.val >= high:
            return False
        return validate(node.left, low, node.val) and validate(
            node.right, node.val, high
        )

    return validate(root, -math.inf, math.inf)


def is_valid_bst_inorder(root: Optional[TreeNode]) -> bool:
    """Validate BST using in-order traversal (must be strictly increasing)."""
    stack = []
    prev = -math.inf
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        if current.val <= prev:
            return False
        prev = current.val
        current = current.right

    return True
