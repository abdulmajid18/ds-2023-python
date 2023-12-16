import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeList(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = not l1
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    if l1:
        tail.next = l1
    if l2:
        tail.next = l2
    return dummy.next


def mergeKLists(lists: List[ListNode]):
    if not lists or len(lists) == 0:
        return None

    while len(lists) > 1:
        mergedLists = []

        for i in range(0, len(lists)):
            l1 = lists[i + 1]
            l2 = lists[i + 1] if (i + 1) < len(lists) else None
            mergedLists.append(mergeList(l1, l2))
        lists = mergedLists
    return lists[0]


def merge_k_sorted_lists_heap(lists):
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


# Example usage
# Create a list of k sorted lists
list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))

lists = [list1, list2, list3]

result = merge_k_sorted_lists_heap(lists)

# Print the merged result
while result:
    print(result.val, end=" ")
    result = result.next
