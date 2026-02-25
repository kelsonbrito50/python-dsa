"""Tests for Validate Binary Search Tree."""

from src.trees.valid_bst import TreeNode, is_valid_bst, is_valid_bst_inorder


class TestValidBST:
    def test_valid_bst(self):
        #     2
        #    / \
        #   1   3
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        assert is_valid_bst(root) is True

    def test_invalid_bst(self):
        #     5
        #    / \
        #   1   4
        #      / \
        #     3   6
        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        assert is_valid_bst(root) is False

    def test_single_node(self):
        assert is_valid_bst(TreeNode(1)) is True

    def test_empty_tree(self):
        assert is_valid_bst(None) is True

    def test_equal_values_invalid(self):
        #     2
        #    / \
        #   2   3
        root = TreeNode(2, TreeNode(2), TreeNode(3))
        assert is_valid_bst(root) is False

    def test_deep_invalid(self):
        #       5
        #      / \
        #     3   7
        #    / \
        #   1   6  <-- 6 > 5, invalid for left subtree
        root = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(6)), TreeNode(7))
        assert is_valid_bst(root) is False


class TestValidBSTInorder:
    def test_valid(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        assert is_valid_bst_inorder(root) is True

    def test_invalid(self):
        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        assert is_valid_bst_inorder(root) is False

    def test_empty(self):
        assert is_valid_bst_inorder(None) is True
