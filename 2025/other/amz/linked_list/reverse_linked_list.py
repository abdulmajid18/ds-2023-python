# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If head is None or only one element, return head
        if not head or not head.next:
            return head

        # Recursive case: Reverse the rest of the list
        new_head = self.reverseList(head.next)

        # After reversing the rest, make the current node's next node point to the current node
        head.next.next = head

        # Set the current node's next to None to indicate it is the new tail
        head.next = None

        return new_head