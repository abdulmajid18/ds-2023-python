class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Solution:

    def invertTree(self, root: TreeNode):
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
