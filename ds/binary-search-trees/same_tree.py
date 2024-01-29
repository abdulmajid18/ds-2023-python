class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def isSameTree(p: TreeNode, q: TreeNode):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.data != q.data:
        return False
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)