from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    length = 0
    tail = head
    while tail:
        length += 1
        tail = tail.next

    target = length // 2
    middle = head

    for _ in range(target):
        middle = middle.next

    return middle


def middleNodePointers(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
