# Definition for a binary tree node.
from typing import Optional, List


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


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode):
        result = []

        def dfs(node, path):
            if node:
                # Add the current node's value to the path
                path += str(node.val)

                # If it's a leaf node, append the path to the result
                if not node.left and not node.right:
                    result.append(path)
                else:
                    # If not a leaf, continue DFS on children with updated path
                    path += "->"  # Add arrow for the next node in the path
                    dfs(node.left, path)
                    dfs(node.right, path)

        # Start DFS from the root
        dfs(root, "")
        return result
