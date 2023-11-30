class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def invert_binary_tree(root):
    if root is not None:
        # Swap the left and right subtrees
        root.left, root.right = root.right, root.left

        # Recursively invert the left and right subtrees
        invert_binary_tree(root.left)
        invert_binary_tree(root.right)


# Example usage:
# Construct a sample binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Invert the binary tree
invert_binary_tree(root)

# The tree after inversion
#       1
#      / \
#     3   2
#        / \
#       5   4
