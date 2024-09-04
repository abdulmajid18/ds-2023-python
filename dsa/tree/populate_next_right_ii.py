from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        # Initialize the queue with the root node
        queue = deque([root])

        while queue:
            # Get the size of the current level
            size = len(queue)

            for i in range(size):
                # Pop the current node from the queue
                node = queue.popleft()

                # Connect the current node's next pointer to the next node in the queue
                # Only if it is not the last node of the current level
                if i < size - 1:
                    node.next = queue[0]

                # Enqueue the left and right children for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return root


from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connect(root):
    if not root:
        return None

    # Initialize the queue with the root node
    queue = deque([root])

    while queue:
        # Get the size of the current level
        size = len(queue)

        prev = None  # This will track the previous node in the level

        for i in range(size):
            node = queue.popleft()

            # If there was a previous node, link it to the current node
            if prev:
                prev.next = node

            prev = node  # Update prev to the current node

            # Enqueue the children of the current node for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # The last node in the current level should point to None
        node.next = None

    return root
