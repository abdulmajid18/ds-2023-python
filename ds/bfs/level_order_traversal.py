from collections import deque


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def levelOrder(root: TreeNode):
    if not root:
        return None
    res = []

    q = deque()
    q.append(root)

    while q:
        qLen = len(q)
        level = []
        for i in range(qLen):
            node = q.popleft()
            level.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        if level:
            res.append(level)
    return res
