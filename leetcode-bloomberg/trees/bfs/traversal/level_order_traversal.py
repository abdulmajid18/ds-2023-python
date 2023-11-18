from collections import deque


class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def levelOrderTraversal(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

# Example usage:
# Create a binary tree and call levelOrderTraversal on the root node
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# levelOrderTraversal(root)
