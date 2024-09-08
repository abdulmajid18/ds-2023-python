from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    cur, stack = root, []
    res = []

    while cur or stack:
        if cur:
            res.append(cur.val)
            stack.append(cur.right)
            cur = cur.left
        else:
            cur = stack.pop()


def preorderTraversal(root):
    if not root:
        return []

    stack, result = [root], []

    while stack:
        node = stack.pop()  # Visit the root node
        result.append(node.val)

        # Push right child first so that left child is processed next
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# Example usage:
# Construct a binary tree:
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(preorderTraversal(root))  # Output: [1, 2, 4, 5, 3]
