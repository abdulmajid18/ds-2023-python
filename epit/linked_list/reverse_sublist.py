from typing import Optional

from epit.linked_list.list_node import ListNode


def reverse_sublist(L: ListNode, start, finish):
    dummy_head = sublist_head = ListNode()
    for _ in range(1, start):
        sublist_head = sublist_head.next

    # reverse sublist
    sublist_iter = sublist_head.next
    for _ in range(finish-start):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = (temp.next,
                                                           sublist_head.next, temp)

    return dummy_head.next


def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    if not head:
        return None

    dummy_head = ListNode(0)
    dummy_head.next = head
    sublist_head = dummy_head

    # Move sublist_head to the node just before the start position
    for _ in range(1, left):
        sublist_head = sublist_head.next

    # Reverse the sublist
    sublist_iter = sublist_head.next
    for _ in range(right - left):
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next






