from collections import deque


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def level_order_traversal(root: TreeNode):
    res = []

    q = deque()
    q.append(root)

    while q:
        qLen = len(q)
        level = []
        for i in range(qLen):
            node = q.popleft()
            if node:
                level.append(node.data)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res