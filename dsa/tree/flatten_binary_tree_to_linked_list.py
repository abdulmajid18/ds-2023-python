from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: TreeNode) -> None:
    # Base case: if the root is None, return immediately
    if not root:
        return

    # Recursively flatten the left and right subtrees
    flatten(root.left)
    flatten(root.right)

    # If there's a left subtree
    if root.left:
        # Store the right subtree temporarily
        temp_right = root.right

        # Move the flattened left subtree to the right
        root.right = root.left
        root.left = None  # Set the left child to None

        # Find the rightmost node in the new right subtree
        current = root.right
        while current.right:
            current = current.right

        # Attach the original right subtree to the end
        current.right = temp_right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Base case: if the root is None, return immediately
        if not root:
            return

        # Initialize a stack and push the root node
        stack = [root]

        while stack:
            # Pop the top node
            current = stack.pop()

            # If there's a right subtree, push it onto the stack
            if current.right:
                stack.append(current.right)

            # If there's a left subtree, push it onto the stack
            if current.left:
                stack.append(current.left)

            # Rewire the current node's right to the next node in the stack
            # (which is the next node in preorder traversal)
            if stack:
                current.right = stack[-1]

            # Set left to None, since we want a right-skewed "linked list"
            current.left = None