class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def mergeTreesInplace(root1, root2):
    # Base case: If one of the nodes is null, return the other node
    if not root1:
        return root2
    if not root2:
        return root1

    # Sum the values of corresponding nodes
    root1.val += root2.val

    # Recursive calls for left and right subtrees
    root1.left = mergeTreesInplace(root1.left, root2.left)
    root1.right = mergeTreesInplace(root1.right, root2.right)

    return root1


def mergeTrees(root1, root2):
    # Base case: If one of the nodes is null, return the other node
    if not root1:
        return root2
    if not root2:
        return root1

    v1 = root1.val if root1 else 0
    v2 = root2.val if root2 else 0

    root = TreeNode(v1 + v2)

    # Recursive calls for left and right subtrees
    root.left = mergeTrees(root1.left if root1 else None, root1.left if root1 else None)
    root.right = mergeTrees(root2.right if root2 else None, root2.right if root2 else None)

    return root
