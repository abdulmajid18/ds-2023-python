# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    # Base case: if the root is None, there's no path, so return False
    if not root:
        return False

    # Check if we're at a leaf node and if the path sum equals targetSum
    if not root.left and not root.right and root.val == targetSum:
        return True

    # Otherwise, recursively check the left and right subtrees with the updated targetSum
    new_sum = targetSum - root.val
    return hasPathSum(root.left, new_sum) or hasPathSum(root.right, new_sum)
