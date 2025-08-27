def closestValue(self, root, target):
    self.closest = root.val
    self.min_diff = float("inf")

    def dfs(node):
        if not node:
            return
        dfs(node.left)

        diff = abs(node.val - target)
        if diff < self.min_diff or (diff == self.min_diff and node.val < self.closest):
            self.min_diff = diff
            self.closest = node.val

        dfs(node.right)

    dfs(root)
    return self.closest
