# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque([root] if root else [])

        while q:
            level = []
            q_len =  len(q)
            for _ in range(q_len):
                cur = q.popleft()
                level.append(cur.val)

                if cur.left:
                    q.append(cur.left)       

                if cur.right:
                    q.append(cur.right)    
            level = reversed(level) if len(res) % 2 == 1 else level
            res.append(level)

        return res