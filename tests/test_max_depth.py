"""Tests for Maximum Depth of Binary Tree."""

from src.trees.max_depth import TreeNode, max_depth, max_depth_iterative


class TestMaxDepth:
    def test_empty_tree(self):
        assert max_depth(None) == 0

    def test_single_node(self):
        assert max_depth(TreeNode(1)) == 1

    def test_balanced_tree(self):
        #       3
        #      / \
        #     9  20
        #       /  \
        #      15   7
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert max_depth(root) == 3

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        assert max_depth(root) == 3

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
        assert max_depth(root) == 4

    def test_depth_two(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert max_depth(root) == 2


class TestMaxDepthIterative:
    def test_empty_tree(self):
        assert max_depth_iterative(None) == 0

    def test_single_node(self):
        assert max_depth_iterative(TreeNode(1)) == 1

    def test_balanced_tree(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert max_depth_iterative(root) == 3

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        assert max_depth_iterative(root) == 3
