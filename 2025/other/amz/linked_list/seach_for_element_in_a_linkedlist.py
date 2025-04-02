class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def searchLinkedList(head, target):
    current = head

    while current:
        if current.val == target:
            return True
        current = current.next

    return False  
