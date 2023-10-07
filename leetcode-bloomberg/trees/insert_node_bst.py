from validate_a_binary_search_tree import BinaryTreeNode
def insertNode(root: BinaryTreeNode, key):
    if root is None:
        return BinaryTreeNode(key)
    if key < root.data:
        root.left = insertNode(root.left, key)
    elif key > root.data:
        root.right = insertNode(root.right, key)
    return currentNode
