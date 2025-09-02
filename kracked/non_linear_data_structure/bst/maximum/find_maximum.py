
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def findMax(root: 'TreeNode') -> int:
    current = root
    while current.right:
        current = current.right
    return current.val

def findMaxRecursion(node):
    if not node.right:
        return node.val
    return findMaxRecursion(node.right)