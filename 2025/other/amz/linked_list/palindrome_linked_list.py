# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindromeBruteForce(head: Optional[ListNode]) -> bool:
    # Step 1: Convert the Linked List into an array (list)
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next

    # Step 2: Check if the array is a palindrome
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1

    return True


def isPalindromeOptimal(head: Optional[ListNode]) -> bool:
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # middle = slow
    # reverse second half
    prev = None
    while slow:
        nxt = slow.next
        slow.next = prev
        prev = slow
        slow = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
