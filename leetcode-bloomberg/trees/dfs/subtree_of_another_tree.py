class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(s: TreeNode, t: TreeNode):
    if not t:
        return True
    if not s and t:
        return False
    if sameTree(s, t):
        return True
    return isSubtree(s.left, t) and isSubtree(s.right, t)


def sameTree(s: TreeNode, t: TreeNode):
    if not s and not t:
        return True
    if s and t and s.val == t.val:
        return sameTree(s.left, t.left) and sameTree(s.right, t.right)
    return False


class TreeNode2:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree2(s, t):
    if not s:
        return False
    if isSameTree2(s, t):
        return True
    return isSubtree2(s.left, t) or isSubtree2(s.right, t)


def isSameTree2(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return p.val == q.val and isSameTree2(p.left, q.left) and isSameTree2(p.right, q.right)
