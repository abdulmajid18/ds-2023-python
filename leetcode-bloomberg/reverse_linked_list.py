from epit.linked_list.list_node import ListNode


def reverse_list_iterative(head: ListNode):
    prev, cur = None, head

    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev


