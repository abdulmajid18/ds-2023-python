class BinaryTreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def isValidBST(root: BinaryTreeNode):
    def valid(node: BinaryTreeNode, left, right):
        if not node:
            return True
        if not (left < node.data < right):
            return False
        return (valid(node.left, left, node.data) and
                valid(node.right, node.data, right))

    return valid(root, float('-inf'), float('inf'))
