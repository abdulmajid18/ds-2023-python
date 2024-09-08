from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: TreeNode):
    if not root:
        return []

    stack, output = [root], []

    while stack:
        node = stack.pop()  # Pop the top node from the stack
        output.append(node.val)  # Add its value to the result list

        # Push left child first, so right child is processed first (pre-order modified)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # Reverse the output to get the correct post-order result
    return output[::-1]


# Example usage:
# Construct a binary tree:
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

print(postorderTraversal(root))  # Output: [4, 5, 2, 3, 1]
