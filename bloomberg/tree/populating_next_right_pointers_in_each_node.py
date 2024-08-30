from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def connectBrute(root):
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



def connect(root):
    if not root:
        return None

    # Start with the leftmost node of the current level
    leftmost = root

    while leftmost.left:
        # Iterate through the nodes of the current level using the next pointers already established
        head = leftmost
        while head:
            # Connect the left child to the right child
            head.left.next = head.right

            # Connect the right child to the next left child of the next node (if available)
            if head.next:
                head.right.next = head.next.left

            # Move to the next node on the same level
            head = head.next

        # Move to the leftmost node of the next level
        leftmost = leftmost.left

    return root
