from collections import defaultdict, deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        # Dictionary to store nodes at each column
        column_table = defaultdict(list)

        # Queue to hold (node, column) pairs for BFS
        queue = deque([(root, 0)])

        # Perform BFS
        while queue:
            node, column = queue.popleft()

            if node:
                # Add node value to the corresponding column
                column_table[column].append(node.val)

                # Process the left child with column - 1
                if node.left:
                    queue.append((node.left, column - 1))

                # Process the right child with column + 1
                if node.right:
                    queue.append((node.right, column + 1))

        # Sort the columns based on the key (column index)
        sorted_columns = sorted(column_table.keys())

        # Build the result from sorted columns
        result = [column_table[col] for col in sorted_columns]

        return result
