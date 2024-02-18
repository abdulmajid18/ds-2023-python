class TreeNode:
    def __int__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxPathSum(root: TreeNode):
    res = [root.val]

    def dfs(root: TreeNode):
        if not root:
            return 0

        leftMax = dfs(root.left)
        rightMax = dfs(root.right)
        leftMax = max(leftMax, 0)
        rightMax = max(rightMax,0)

        res[0] = max(res[0], root.val + leftMax + rightMax)

        return root.val + max(leftMax, rightMax)
    dfs(root)
    return res[0]