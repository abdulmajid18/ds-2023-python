# Post-order iterative traversal. The nodes' values are appended to the result list in traversal order

"""
In preorder and inorder traversals, after popping the stack element we do not need to visit the same vertex again. But in postorder traversal,
each node is visited twice. That means, after processing the left subtree we will visit the current node and after processing the right subtree we
will visit the same current node. But we should be processing the node during the second visit. Here the problem is how to differentiate
whether we are returning from the left subtree or the right subtree.
"""


class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderIterative(root, result):
    if not root:
        return
    visited = set()
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            if node.right and not node.right in visited:
                stack.append(node)
                node = node.right
            else:
                visited.add(node)
                result.append(node.data)
                node = None


def postOrderIterative2(root: TreeNode):
    stack = [root]
    vist = [False]
    res = []

    while stack:
        cur, v = stack.pop(), vist.pop()
        if cur:
            if v:
                res.append(cur.val)
            else:
                stack.append(cur)
                vist.append(True)
                stack.append(cur.right)
                vist.append(False)
                stack.append(cur.left)
                vist.append(False)

