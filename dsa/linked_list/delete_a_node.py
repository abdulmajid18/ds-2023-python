# Definition for a singly linked list node.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: None
        """
        # Copy the value from the next node to the current node
        node.val = node.next.val
        # Bypass the next node by pointing to the node after next
        node.next = node.next.next
