# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque([root])

        res = []

        while q:
            q_len = len(q)
            level_res = []

            for _ in range(q_len):
                node = q.popleft()
                if node:
                    level_res.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level_res:
                res.append(level_res)
        res.reverse()
        return res

