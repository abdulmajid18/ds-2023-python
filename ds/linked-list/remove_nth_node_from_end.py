class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head, n):
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy

    # Move the fast pointer n+1 steps ahead
    for _ in range(n + 1):
        fast = fast.next

    # Move both pointers until the fast pointer reaches the end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the n-th node
    slow.next = slow.next.next

    return dummy.next


# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
result = remove_nth_from_end(head, n)

# Print the modified linked list
while result:
    print(result.val, end=" -> ")
    result = result.next


def remove_nth_from_end_2(head: ListNode, n):
    dummy = ListNode(0, head)
    left = dummy
    right = head

    while n > 0 and right:
        right = right.next
        n -= 1

    while right:
        right = right.next
        left = left.next

    left.next = left.next.next
    return dummy.next
