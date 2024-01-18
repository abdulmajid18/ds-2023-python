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


class Solution:
    def recoverTree(self, root):
        self.first_element = None
        self.second_element = None
        self.prev_element = TreeNode(float('-inf'))

        def inorder_traversal(node):
            if node:
                inorder_traversal(node.left)

                # Check if the current node violates the BST property
                if not self.first_element and self.prev_element.val >= node.val:
                    self.first_element = self.prev_element
                if self.first_element and self.prev_element.val >= node.val:
                    self.second_element = node

                self.prev_element = node

                inorder_traversal(node.right)

        inorder_traversal(root)

        # Swap the values of the two elements to recover the BST
        if self.first_element and self.second_element:
            self.first_element.val, self.second_element.val = self.second_element.val, self.first_element.val
