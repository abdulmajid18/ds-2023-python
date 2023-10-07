class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postOrder1(root: TreeNode, res):
    if not root:
        return
    postOrder1(root.left)
    postOrder1(root.right)
    res.append(root.val)


def postOrder2(root: TreeNode, res):
    if not root:
        return
    postOrder2(root.left)
    postOrder2(root.right)
    res.append(root.val)
