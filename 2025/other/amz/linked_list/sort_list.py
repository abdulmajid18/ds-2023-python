# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Step 1: Find the middle of the linked list using the slow/fast pointer approach
        def get_middle(head):
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # Step 2: Split the list into two halves
        def merge(left, right):
            dummy = ListNode()
            tail = dummy
            while left and right:
                if left.val < right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            if left:
                tail.next = left
            if right:
                tail.next = right
            return dummy.next

        middle = get_middle(head)
        left = head
        right = middle.next
        middle.next = None  # Split the list into two parts

        # Step 3: Recursively sort the two halves
        left = self.sortList(left)
        right = self.sortList(right)

        # Step 4: Merge the sorted halves
        return merge(left, right)
