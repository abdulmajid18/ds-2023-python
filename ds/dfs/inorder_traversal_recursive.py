class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inOrderRecursive(root: TreeNode, result):
    res = []

    def inorder(root: TreeNode):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res

