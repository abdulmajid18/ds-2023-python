# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root or root.val == val:
        return root
    elif val < root.val:
        return self.searchBST(root.left, val)
    else:
        return self.searchBST(root.right, val)


def searchBSIterative(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    curr = root
    while curr:
        if curr.val == val:
            return curr
        elif val < curr.val:
            curr = curr.left
        else:
            curr = curr.right
    return None


class Solution:
    pass
