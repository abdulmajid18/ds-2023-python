class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def zigZagLevelOrder(root: TreeNode):
    from collections import deque

    queue = deque()
    # queue = [ [root] if root else []]
    queue.append(root)
    result = []

    while queue:
        # build level by level
        level = []
        for i in range(len(queue)):
            node: TreeNode = queue.popleft()
            level.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        level = reversed(level) if len(result) % 2 else level
        result.append(level)
    return result