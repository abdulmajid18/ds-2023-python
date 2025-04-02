class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getLength(head):
    count = 0
    current = head  # Start from the head node

    while current:
        count += 1
        current = current.next  # Move to the next node

    return count


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(getLength(head))