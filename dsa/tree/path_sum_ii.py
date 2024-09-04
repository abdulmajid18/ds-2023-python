# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def dfs(node, current_path, remaining_sum):
            if not node:
                return

            # Include the current node in the path
            current_path.append(node.val)
            remaining_sum -= node.val

            # If it's a leaf node and the remaining_sum is zero, we've found a valid path
            if not node.left and not node.right and remaining_sum == 0:
                # Append a copy of the current path to the result list
                result.append(list(current_path))

            # Recurse to the left and right children
            dfs(node.left, current_path, remaining_sum)
            dfs(node.right, current_path, remaining_sum)

            # Backtrack: remove the current node from the path before returning
            current_path.pop()

        result = []
        dfs(root, [], targetSum)
        return result
