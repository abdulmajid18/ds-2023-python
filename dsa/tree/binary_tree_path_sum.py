# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root: return ""
        res = []
        self.dfsHelper(root, "", res)
        return res

    def dfsHelper(self, root, tempPath, res):
        if not root: return

        if not root.left and not root.right:
            res.append(tempPath + str(root.val))
            return

        if root.left:
            self.dfsHelper(root.left, tempPath + str(root.val) + "->", res)

        if root.right:
            self.dfsHelper(root.right, tempPath + str(root.val) + "->", res)