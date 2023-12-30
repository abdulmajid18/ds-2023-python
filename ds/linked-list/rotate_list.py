class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head, k):
    if not head or k == 0:
        return head

    # Find the length of the linked list
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # Calculate the effective rotation value
    k = k % length

    if k == 0:
        return head  # No rotation needed

    # Find the new head position after rotation
    new_head_pos = length - k

    # Update pointers to achieve rotation
    tail.next = head  # Connect the tail to the original head
    new_tail = head
    for _ in range(new_head_pos - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None  # Set the new tail's next to None

    return new_head

# Example usage:
# Construct a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
k = 2
rotated_head = rotateRight(head, k)

# Print the rotated linked list
while rotated_head:
    print(rotated_head.val, end=" -> ")
    rotated_head = rotated_head.next


def rotate_right(head:ListNode, k):
    if not head:
        return head

    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1

    k = k % length

    if k == 0:
        return head
    cur = head
    for i in range(length - k - 1):
        cur = cur.next
    new_head = cur.next
    cur.next = None
    tail.next = head
    return new_head
