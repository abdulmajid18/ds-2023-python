class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertAtEnd(self, head: ListNode, x: int) -> ListNode:
        new_node = ListNode(x)

        # If the list is empty, the new node becomes the head
        if not head:
            return new_node

        # Traverse to the last node
        current = head
        while current.next:
            current = current.next

        # Link the last node to the new node
        current.next = new_node

        return head  # Return the updated linked list


def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
sol = Solution()
new_head = sol.insertAtEnd(head, 6)

printLinkedList(new_head)  # Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
