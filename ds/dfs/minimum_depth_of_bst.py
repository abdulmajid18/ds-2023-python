class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minDepth(root):
    if not root:
        return 0

    # If the current node is a leaf node, return 1
    if not root.left and not root.right:
        return 1

    # If left subtree is empty, find the minimum depth of the right subtree
    if not root.left:
        return minDepth(root.right) + 1

    # If right subtree is empty, find the minimum depth of the left subtree
    if not root.right:
        return minDepth(root.left) + 1

    # If both subtrees are non-empty, find the minimum depth of both subtrees
    return min(minDepth(root.left), minDepth(root.right)) + 1


# Example usage:
# Construct a binary tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print("Minimum depth of the binary tree:", minDepth(root))
