class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')

        def maxDownSum(node):
            if not node:
                return 0

            # Compute the maximum path sum "down" from the left and right child nodes
            left_max = max(maxDownSum(node.left), 0)
            right_max = max(maxDownSum(node.right), 0)

            # Calculate the maximum path sum with the current node as the inflection point
            current_sum = node.val + left_max + right_max

            # Update the global maximum sum if the current path sum is greater
            self.max_sum = max(self.max_sum, current_sum)

            # Return the maximum sum path going down from the current node
            return node.val + max(left_max, right_max)

        # Start the DFS traversal from the root
        maxDownSum(root)

        return self.max_sum


# Example Usage:
# Let's assume we have a binary tree with root node defined as follows:
#      1
#     / \
#    2   3
# The maximum path sum in this tree is 6 (2 -> 1 -> 3).

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

solution = Solution()
print(solution.maxPathSum(root))  # Output: 6
