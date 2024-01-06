class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head: ListNode) -> ListNode:
    current = head

    while current and current.next:
        if current.val == current.next.val:
            # Skip the next node by updating the current node's next pointer
            current.next = current.next.next
        else:
            # Move to the next node
            current = current.next

    return head


# Example usage:
# Assuming you have a sorted linked list: 1 -> 1 -> 2 -> 3 -> 3
linked_list = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3)))))

print("Original Linked List:")
current_node = linked_list
while current_node:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")

new_linked_list = delete_duplicates(linked_list)

print("\nLinked List after removing duplicates:")
current_node = new_linked_list
while current_node:
    print(current_node.val, end=" -> ")
    current_node = current_node.next
print("None")
