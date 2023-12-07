class BinaryTreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def iterativeDFS(root):
    if root is None:
        return

    stack = [root]

    while stack:
        node = stack.pop()
        print(node.data, end=" ")

        # Push right child first (since it needs to be processed after left child)
        if node.right:
            stack.append(node.right)

        # Push left child
        if node.left:
            stack.append(node.left)

# Example usage:
# Create a binary tree and call iterativeDFS on the root node
# root = BinaryTreeNode(1)
# root.left = BinaryTreeNode(2)
# root.right = BinaryTreeNode(3)
# root.left.left = BinaryTreeNode(4)
# root.left.right = BinaryTreeNode(5)
# iterativeDFS(root)
