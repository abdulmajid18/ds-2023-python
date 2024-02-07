# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructTree(self, preOrder: List[int], inOrder: List[int]):
        if not preOrder or not inOrder:
            return None

        root = TreeNode(val=preOrder[0])
        mid = inOrder.index(root.val)
        root.left = self.constructTree(preOrder[1:mid + 1], inOrder[:mid])
        root.right = self.constructTree(preOrder[mid + 1:], inOrder[mid:])
        return root


