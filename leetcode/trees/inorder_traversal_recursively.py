class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode):
    res = []

    def inorder(root):
        if not root:
            return
        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res


class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def inOrder(self, root):
        if root is None:
            return
        self.inOrder(root.left)
        print(root.data, sep="-->", end="-->")
        self.inOrder(root.right)

    def inOrder2(self, root):
        if root is None:
            return
        self.inOrder2(root.right)
        print(root.data, sep="-->", end="-->")
        self.inOrder2(root.left)
