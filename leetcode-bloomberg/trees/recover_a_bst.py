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

    def recoverMorisTraversal(self, root: TreeNode):
        previousNode: TreeNode = None
        arr = []

        def inOrder(node: TreeNode):
            if not node:
                return

            inOrder(node.left)
            nonlocal previousNode
            if previousNode and previousNode.val > node.val:
                if len(arr) == 0:
                    arr.append(previousNode)
            inOrder(node.right)

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

