# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(root):
        if root:
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        return

    dfs(root)
    return res