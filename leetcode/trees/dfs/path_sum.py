class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasPathSum(root, targetSum):
    # Helper function for DFS traversal
    def dfs(node, current_sum):
        # Base case: If the node is None, return False
        if not node:
            return False

        # Update the current sum
        current_sum += node.val

        # If it's a leaf node and the current sum equals the targetSum, return True
        if not node.left and not node.right:
            return current_sum == targetSum

        # Recursive calls for the left and right children
        left_result = dfs(node.left, current_sum)
        right_result = dfs(node.right, current_sum)

        # Return True if either left or right subtree has a path with the targetSum
        return left_result or right_result

    # Start DFS traversal from the root with an initial current sum of 0
    return dfs(root, 0)
