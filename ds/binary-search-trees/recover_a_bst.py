class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverBST(self, root: TreeNode):
        self.temp = []

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            self.temp.append(node)
            dfs(node.right)

        dfs(root)
        srt = sorted(n.val for n in self.temp)

        for i in range(len(srt)):
            self.temp[i].val = srt[i]
        return self.temp



    def reversalMoris(self, root: TreeNode):
        curr = root
        prev: TreeNode = TreeNode(val=float('-inf'))
        stack = []
        replace = []

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            temp = stack.pop()
            if temp.val < prev.val:
                replace.append(prev, temp)

            prev = temp
            curr = temp.right
        replace[0][0].val, replace[-1][1].val = replace[-1][1].val, replace[0][0].val

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Initialize variables to keep track of nodes to be swapped
        first, second, prev = None, None, None

        # Helper function for in-order traversal to find the misplaced nodes
        def inorder_traversal(node):
            nonlocal first, second, prev

            if not node:
                return

            inorder_traversal(node.left)

            # Check for misplaced nodes
            if prev and prev.val > node.val:
                if not first:
                    first = prev
                second = node

            prev = node

            inorder_traversal(node.right)

        # Perform in-order traversal to identify misplaced nodes
        inorder_traversal(root)

        # Swap the values of the misplaced nodes
        first.val, second.val = second.val, first.val
