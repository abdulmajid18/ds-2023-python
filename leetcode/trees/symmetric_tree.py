class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode):
        def dfs(left: TreeNode, right: TreeNode):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.data == right.data and
                    dfs(left.left, left.right) and
                    dfs(right.left, right.right))
        return dfs(root.left, root.right)