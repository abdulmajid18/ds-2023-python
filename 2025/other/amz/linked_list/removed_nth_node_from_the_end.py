class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionBrute:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Step 1: Find the length of the list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        # Step 2: Find the (length - n)th node
        dummy = ListNode(0, head)  # Dummy node to handle edge cases (like removing head)
        prev = dummy
        target_index = length - n

        for _ in range(target_index):
            prev = prev.next  # Move to the node before the target

        # Step 3: Remove the target node
        prev.next = prev.next.next

        return dummy.next  # Return new head


from typing import Optional


class Solution:
    def removeNthFromEndOptimized(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)  # Dummy node to handle edge cases
        left = dummy
        right = dummy

        # Move `right` pointer `n+1` steps ahead (to maintain a gap of `n`)
        for _ in range(n + 1):
            right = right.next

        # Move both pointers until `right` reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the nth node
        left.next = left.next.next

        return dummy.next  # Return new head (skip dummy)

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to handle edge cases
        dummy.next = head
        left = dummy
        right = dummy

        # Use your existing while loop to move `right` n steps ahead
        while n:
            right = right.next
            n -= 1

        # Move `right` one more step so that there's a gap of `n+1`
        right = right.next

        # Move both pointers until `right` reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the Nth node
        left.next = left.next.next

        return dummy.next  # Return new head
