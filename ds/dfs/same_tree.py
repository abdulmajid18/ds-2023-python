class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Base case: If both trees are None, they are the same
        if not p and not q:
            return True

        # If one tree is None and the other is not, they are different
        if not p or not q:
            return False

        # Check if the current nodes have the same value
        if p.val != q.val:
            return False

        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
