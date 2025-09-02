
def tree_maximum(node):
    while node.right:
        node = node.right
    return node

def tree_predecessor(x):
    # Case 1: left subtree exists
    if x.left:
        return tree_maximum(x.left)

    # Case 2: walk up until x is right child
    y = x.parent
    while y and x == y.left:
        x = y
        y = y.parent
    return y
