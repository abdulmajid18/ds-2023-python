# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If head is None or only one element, return head
        if not head or not head.next:
            return head

        # Recursive case: Reverse the rest of the list
        new_head = self.reverseList(head.next)

        head.next.next = head

        # Set the current node's next to None to indicate it is the new tail
        head.next = None

        return new_head
