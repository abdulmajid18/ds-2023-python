# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first, second, prev = None, None, None

        # Helper function for in-order traversal to find the misplaced nodes
        def inorder_traversal(node):
            nonlocal first, second, prev

            if not node:
                return

            inorder_traversal(node.left)

            # Check for misplaced nodes
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node

            prev = node

            inorder_traversal(node.right)

        # Perform in-order traversal to identify misplaced nodes
        inorder_traversal(root)

        # Swap the values of the misplaced nodes
        first.val, second.val = second.val, first.val
