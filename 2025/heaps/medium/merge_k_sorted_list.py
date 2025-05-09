import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []

    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next


from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

    # Helper function to print the linked list
    def __str__(self):
        return f"{self.val} -> {self.next}"


def mergeKListsTwo(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # Helper function to merge two sorted lists
    def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next

    if not lists:
        return None

    while len(lists) > 1:
        merged_list = []
        for i in range(0, len(lists), 2):
            # Merge pairs of lists
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_list.append(mergeTwoLists(l1, l2))
        lists = merged_list
    return lists[0]
