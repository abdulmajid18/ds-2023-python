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
