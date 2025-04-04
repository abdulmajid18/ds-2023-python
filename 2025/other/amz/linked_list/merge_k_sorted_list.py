# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        heap = []

        import heapq

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Helper function to merge two sorted lists
        def merge_two_lists(l1, l2):
            dummy = ListNode()
            current = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    current.next = l1
                    l1 = l1.next
                else:
                    current.next = l2
                    l2 = l2.next
                current = current.next
            current.next = l1 if l1 else l2  # Append the remaining nodes
            return dummy.next

        # If lists is empty, return None
        if not lists:
            return None

        # Recursive function to divide and conquer
        def merge_lists_in_pairs(lists):
            if len(lists) == 1:
                return lists[0]
            mid = len(lists) // 2
            left = merge_lists_in_pairs(lists[:mid])
            right = merge_lists_in_pairs(lists[mid:])
            return merge_two_lists(left, right)

        return merge_lists_in_pairs(lists)
