class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_linked_list_iterative(head):
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverse_linked_list_iterative(head)

# Print the reversed linked list
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next


def reverse_linked_list_recursive_1(head):
    # Base case: an empty list or a single node
    if not head:
       return None

    newHead = head
    if head.next:
        newHead = reverse_linked_list_recursive_1(head.next)
        head.next.next = head
    head.next = None
    return newHead


# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverse_linked_list_recursive_1(head)

# Print the reversed linked list
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next


