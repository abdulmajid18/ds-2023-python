# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicatesBruteForce(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return head

    seen = set()  # Store unique values
    dummy = ListNode(0)  # Dummy node for new list
    tail = dummy
    current = head

    while current:
        if current.val not in seen:
            seen.add(current.val)
            tail.next = ListNode(current.val)  # Create new node
            tail = tail.next
        current = current.next

    return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    current = head

    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head