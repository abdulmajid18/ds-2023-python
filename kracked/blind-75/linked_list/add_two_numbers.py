class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Initialize a dummy node to simplify the result list creation
        dummy = ListNode()
        current = dummy
        carry = 0

        # Traverse both lists
        while l1 or l2 or carry:
            # Get the values from the current nodes or 0 if the list has ended
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)

            # Move to the next nodes
            current = current.next
            # l1 = l1.next if l1 else None
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy.next
