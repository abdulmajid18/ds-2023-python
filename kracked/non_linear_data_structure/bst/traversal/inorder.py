# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(root, res):
        if root:
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        return

    dfs(root, res)
    return res


def iterativeInOrderTraversal(root):

    res, stack = [], []

    curr = root

    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        res.append(curr.val)

        curr = curr.right

    return res