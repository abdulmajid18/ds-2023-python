# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def checkBalance(node: TreeNode):
            if not node:
                return True, 0

            left_balanced, left_height = checkBalance(node.left)
            right_balanced, right_height = checkBalance(node.right)

            balanced = (left_balanced and right_balanced and abs(left_height - right_height) <= 1)
            height = max(left_height, right_height) + 1

            return balanced, height

        balanced, _ = checkBalance(root)
        return balanced


