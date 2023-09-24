class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next


def remove_nth_from_end_1(head: ListNode, n: int):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # Move the right pointer n nodes ahead
    for _ in range(n):
        if right is None:
            return None  # Handle the case where n is greater than the length of the list
        right = right.next

    # Move both left and right pointers simultaneously
    while right.next is not None:
        left = left.next
        right = right.next

    # Remove the nth node by updating the next reference of the left node
    left.next = left.next.next

    return dummy.next  # Return the updated linked list


def remove_nth_from_end_3(head: ListNode, n: int):
    left = head
    right = head

    # Move the right pointer n nodes ahead
    for _ in range(n):
        if right is None:
            return None  # Handle the case where n is greater than the length of the list
        right = right.next

    # Handle the special case of removing the head node
    if right is None:
        return head.next

    # Move both left and right pointers simultaneously
    while right.next is not None:
        left = left.next
        right = right.next

    # Remove the nth node by updating the next reference of the left node
    left.next = left.next.next

    return head  # Return the updated linked list

