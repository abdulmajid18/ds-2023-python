class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrderIterative(root: TreeNode, result):
    if not root:
        return
    stack = []
    result = []
    node: TreeNode = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.val)
            node = node.right


def inOrderTraversal(root: TreeNode):
    stack = []
    cur = root
    res = []

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        res.append(cur.val)
        cur = cur.right
    return res
