
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findMinimumRecursion(node: TreeNode):
    if not node.left:
        return node.val
    return findMinimumRecursion(node.left)


def findMinimum(root: 'TreeNode') -> int:
    current = root
    while current.left:
        current = current.left
    return current.val