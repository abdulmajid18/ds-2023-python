
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


class BNode:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right


def isValidBSTIterative(root: BNode):
    if not root:
        return True

    queue = [BNode(root, float('-inf'), float('inf'))]

    while queue:
        b = queue.pop(0)
        if b.node.val <= b.left or b.node.val >= b.right:
            return False
        if b.node.left:
            queue.append(BNode(b.node.left, b.left, b.node.val))
        if b.node.right:
            queue.append(BNode(b.node.right, b.node.val, b.right))

    return True


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST2(root):
    return isValidBSTRecursive(root, float('-inf'), float('inf'))


def isValidBSTRecursive(node, min_val, max_val):
    if not node:
        return True

    if node.val <= min_val or node.val >= max_val:
        return False

    return (isValidBSTRecursive(node.left, min_val, node.val) and
            isValidBSTRecursive(node.right, node.val, max_val))

def isValidBSTRecursive2(node, min_val, max_val):
    if not node:
        return True

    if not (node.val < min_val and node.val > max_val):
        return False

    return (isValidBSTRecursive(node.left, min_val, node.val) and
            isValidBSTRecursive(node.right, node.val, max_val))

# Example usage:
# Construct a binary tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

print(isValidBST(root))  # Output: True (It's a valid BST)
