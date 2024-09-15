class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    # Step 1: Traverse the linked list and store values in an array
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next

    # Step 2: Use the helper function to check if the array is a palindrome
    return is_palindrome_array(values)


def is_palindrome_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True


# Helper function to create a linked list from a list
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


# Example usage
head = create_linked_list([1, 2, 2, 1])
print(isPalindrome(head))  # Output: True

head = create_linked_list([1, 2, 3, 4])
print(isPalindrome(head))  # Output: False
