from typing import Optional
import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> None:
        res = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            queue_len = len(queue)
            level = []

            for i in range(queue_len):
                cur = queue.popleft()
                if cur:
                    level.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
            if level:
                res.append(level)
        return res




