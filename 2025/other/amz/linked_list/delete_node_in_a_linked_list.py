class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(node):
    if node and node.next:
        node.val = node.next.val
        node.next = node.next.next
