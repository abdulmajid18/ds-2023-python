class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderRecursively1(root: TreeNode):
    result = []
    if not root:
        return
    cur = root
    result.append(cur.val)
    preorderRecursively1(cur.left)
    preorderRecursively1(cur.right)


def preorderRecursively2(root: TreeNode):
    result = []
    if not root:
        return
    cur = root
    result.append(cur.val)
    preorderRecursively2(cur.left)
    preorderRecursively2(cur.right)
