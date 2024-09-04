# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # The first element of preorder is the root
    root_val = preorder[0]
    root = TreeNode(root_val)

    # Find the index of the root in inorder
    mid = inorder.index(root_val)

    # Recursively build the left subtree and right subtree
    root.left = buildTree(preorder[1:mid + 1], inorder[:mid])
    root.right = buildTree(preorder[mid + 1:], inorder[mid + 1:])

    return root
