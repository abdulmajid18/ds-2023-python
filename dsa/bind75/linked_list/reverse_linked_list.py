# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None or it's the last node
        if not head or not head.next:
            return head

        # Reverse the rest of the list recursively
        new_head = self.reverseList(head.next)

        # Reverse the current node
        head.next.next = head
        head.next = None

        return new_head
