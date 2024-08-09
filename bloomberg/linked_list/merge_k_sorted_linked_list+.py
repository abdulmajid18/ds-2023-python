# Definition for singly-linked list.
from typing import List, Optional
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Define comparison for heapq to work on ListNode objects
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        # Initialize the heap with the head nodes of all lists
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, lists[i])

        dummy = ListNode(0)
        tail = dummy

        while min_heap:
            # Extract the smallest node from the heap
            smallest_node = heapq.heappop(min_heap)
            tail.next = smallest_node
            tail = tail.next

            # If the extracted node has a next node, push it into the heap
            if smallest_node.next:
                heapq.heappush(min_heap, smallest_node.next)

        return dummy.next


def mergeKListsHeap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Create a min heap
    min_heap = []

    # Push the first element from each list into the heap
    for i, l in enumerate(lists):
        if l:
            heapq.heappush(min_heap, (l.val, i, l))

    # Dummy node to simplify the code
    dummy = ListNode()
    current = dummy

    while min_heap:
        # Pop the smallest element from the heap
        val, i, node = heapq.heappop(min_heap)

        # Append the node to the result list
        current.next = node
        current = current.next

        # Move to the next element in the list
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dummy.next