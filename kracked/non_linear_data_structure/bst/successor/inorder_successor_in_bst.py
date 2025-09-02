class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderSuccessor(root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
    successor = None

    if p.right:
        # Case 1: successor is the leftmost node in right subtree
        node = p.right
        while node.left:
            node = node.left
        return node

    # Case 2: walk from root
    node = root
    while node:
        if p.val < node.val:
            successor = node
            node = node.left
        else:
            node = node.right

    return successor
