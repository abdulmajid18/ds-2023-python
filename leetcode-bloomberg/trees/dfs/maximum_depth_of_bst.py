class BNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDeptDFSRecursion(root: BNode):
    if not root:
        return 0

    return 1 + max(maxDeptDFSRecursion(root.right),
                   maxDeptDFSRecursion(root.left))


def maxDeptBFS(root: BNode):
    if not root:
        return 0
    from collections import deque
    queue = deque([root])
    level = 0

    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        level += 1
    return level


def maxDeptDFSIterative(root: BNode):
    if not root:
        return 0
    stack = [[root, 1]]
    res = 1
    while stack:
        node, depth = stack.pop()
        if node:
            res = max(res, depth)
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
    return res



