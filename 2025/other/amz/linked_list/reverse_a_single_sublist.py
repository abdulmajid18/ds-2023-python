"""
Problem Statement:
Given the head of a singly linked list and two integers left and right (1-based index),
reverse the sublist between positions left and right, and return the modified linked list.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if not head or left == right:
        return head

    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(left - 1):
        prev = prev.next

    curr = prev.next
    next_node = None
    prev_reversed = None

    for _ in range(right - left + 1):
        next_node = curr.next  # Save next node
        curr.next = prev_reversed  # Reverse pointer
        prev_reversed = curr  # Move prev forward
        curr = next_node  # Move curr forward

        # Step 3: Reconnect the reversed sublist
    prev.next.next = curr  # Connect tail of reversed sublist to right+1 node
    prev.next = prev_reversed  # Connect node before left to new head

    return dummy.next  # Return new head (dummy.next)


