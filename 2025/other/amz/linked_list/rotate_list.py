# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length, tail = 1, head

        while tail.next:
            length += 1
            tail = tail.next

        k = k % length
        if k == 0:
            return head

        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head

        return newHead
