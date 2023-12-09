class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_beginning(head, n):
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head

    # Move to the (n-1)-th node
    prev = dummy
    for _ in range(n - 1):
        if prev.next:
            prev = prev.next
        else:
            # Handle the case where n is greater than the length of the list
            return dummy.next

    # Remove the Nth node
    if prev.next:
        prev.next = prev.next.next

    return dummy.next

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
result = remove_nth_from_beginning(head, n)

# Print the modified linked list
while result:
    print(result.val, end=" -> ")
    result = result.next
