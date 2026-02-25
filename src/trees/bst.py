"""
Binary Search Tree — Insert, Search, Traversals.

Average: O(log n) insert/search
Worst:   O(n) for skewed trees
"""


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None


class BST:
    def __init__(self) -> None:
        self.root: TreeNode | None = None

    def insert(self, val: int) -> None:
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert(self.root, val)

    def _insert(self, node: TreeNode, val: int) -> None:
        if val < node.val:
            if node.left:
                self._insert(node.left, val)
            else:
                node.left = TreeNode(val)
        else:
            if node.right:
                self._insert(node.right, val)
            else:
                node.right = TreeNode(val)

    def search(self, val: int) -> bool:
        return self._search(self.root, val)

    def _search(self, node: TreeNode | None, val: int) -> bool:
        if not node:
            return False
        if val == node.val:
            return True
        if val < node.val:
            return self._search(node.left, val)
        return self._search(node.right, val)

    def inorder(self) -> list[int]:
        """In-order traversal — returns sorted values."""
        result: list[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: TreeNode | None, result: list[int]) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)
