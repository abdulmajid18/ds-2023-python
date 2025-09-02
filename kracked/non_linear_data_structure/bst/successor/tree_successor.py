
def tree_minimum(node):
    while node.left:
        node = node.left
    return node

def tree_successor(x):
    # Case 1: right subtree exists
    if x.right:
        return tree_minimum(x.right)

    # Case 2: walk up until x is left child
    y = x.parent
    while y and x == y.right:
        x = y
        y = y.parent
    return y
