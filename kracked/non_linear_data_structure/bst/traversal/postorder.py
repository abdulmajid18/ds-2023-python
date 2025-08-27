from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    res = []

    def dfs(node):
        if not node:
            return
        dfs(node.left)
        dfs(node.right)
        res.append(node.val)

    dfs(root)
    return res

def postorderTraversalIterative(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return

    stack, res = [root], []

    while stack:
        node = stack.pop()
        res.append(node.val)

        if node.left:
            stack.append(node.left)

        if node.right:
            stack.append(node.right)

    return res[::-1]
