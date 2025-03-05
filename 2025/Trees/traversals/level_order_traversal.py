# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional, List


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        res = []
        q = deque([root])

        while q:
            queue_len = len(q)
            level_res = []
            for i in range(queue_len):
                node = q.popleft()
                if node:
                    level_res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level_res:
                res.append(level_res)
        return res



