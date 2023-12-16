import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_sorted_lists(lists):
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

result = merge_k_sorted_lists(lists)

# Print the merged result
while result:
    print(result.val, end=" ")
    result = result.next
