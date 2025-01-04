class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# def swap_pairs(head):
#     dummy = ListNode(0, head)
#     prev, curr = dummy,
def swapPairs(head):
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    dummy.next = head
    current = dummy

    while current.next and current.next.next:
        # Nodes to be swapped
        first = current.next
        second = current.next.next

        # Swapping
        # reverse this pair
        first.next = second.next
        second.next = first
        current.next = second

        # Move to the next pair
        current = current.next.next

    return dummy.next

# Example usage:
# Construct a linked list: 1 -> 2 -> 3 -> 4
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
result = swapPairs(head)
# After swapping pairs: 2 -> 1 -> 4 -> 3
