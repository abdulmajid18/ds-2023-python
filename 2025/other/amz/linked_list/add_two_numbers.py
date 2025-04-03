# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0  # Get value from l1 (or 0 if None)
            val2 = l2.val if l2 else 0  # Get value from l2 (or 0 if None)

            total = val1 + val2 + carry
            carry = total // 10  # Extract carry
            current.next = ListNode(total % 10)  # Create a new node with the sum digit

            current = current.next  # Move forward in result list
            if l1: l1 = l1.next  # Move forward in l1
            if l2: l2 = l2.next  # Move forward in l2

        return dummy.next

