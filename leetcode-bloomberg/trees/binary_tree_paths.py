from typing import Optional, List


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


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


class Solution2(object):
    def binaryTreePaths(self, root):
        if not root: return ""
        stack = [(root, "")]
        res = []

        while stack:
            node, curPath = stack.pop()
            if not node.left and not node.right:
                res.append(curPath + str(node.val))
            if node.left:
                stack.append((node.left, curPath + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, curPath + str(node.val) + "->"))
        return res
