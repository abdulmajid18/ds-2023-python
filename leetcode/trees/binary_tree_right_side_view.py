class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rightSideView(self, root: TreeNode):
        from collections import deque
        result = []
        queue = deque([root if root else []])

        while queue:
            rightSide = None
            for i in range(len(queue)):
                node: TreeNode = queue.popleft()
                if node:
                    rightSide = node
                    queue.append(node.left)
                    queue.append(node.right)
            if rightSide:
                result.append(rightSide.val)
        return result


