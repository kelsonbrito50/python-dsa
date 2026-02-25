"""Tests for level order traversal and max depth."""

from src.trees.level_order import TreeNode, level_order, max_depth


def _build_tree(vals: list) -> TreeNode | None:
    """Build tree from level-order list (None = missing node)."""
    if not vals:
        return None
    root = TreeNode(vals[0])
    queue = [root]
    i = 1
    while i < len(vals):
        node = queue.pop(0)
        if i < len(vals) and vals[i] is not None:
            node.left = TreeNode(vals[i])
            queue.append(node.left)
        i += 1
        if i < len(vals) and vals[i] is not None:
            node.right = TreeNode(vals[i])
            queue.append(node.right)
        i += 1
    return root


class TestLevelOrder:
    def test_basic(self):
        root = _build_tree([3, 9, 20, None, None, 15, 7])
        assert level_order(root) == [[3], [9, 20], [15, 7]]

    def test_empty(self):
        assert level_order(None) == []

    def test_single_node(self):
        assert level_order(TreeNode(1)) == [[1]]

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        assert level_order(root) == [[1], [2], [3]]

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        assert level_order(root) == [[1], [2], [3]]

    def test_complete_tree(self):
        root = _build_tree([1, 2, 3, 4, 5, 6, 7])
        assert level_order(root) == [[1], [2, 3], [4, 5, 6, 7]]


class TestMaxDepth:
    def test_basic(self):
        root = _build_tree([3, 9, 20, None, None, 15, 7])
        assert max_depth(root) == 3

    def test_empty(self):
        assert max_depth(None) == 0

    def test_single_node(self):
        assert max_depth(TreeNode(1)) == 1

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        assert max_depth(root) == 4

    def test_balanced(self):
        root = _build_tree([1, 2, 3, 4, 5, 6, 7])
        assert max_depth(root) == 3
