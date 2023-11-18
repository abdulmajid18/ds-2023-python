class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preOrderTraversal1(root: TreeNode):
    if not root:
        return
    stack = []
    result = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result

def preOrderTraversal2(root: TreeNode):
    cur, stack = root, []
    res = []

    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()