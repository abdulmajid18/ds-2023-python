from epit.linked_list.list_node import ListNode


def reverse_sublist(head: ListNode, left, right):
    dummy = ListNode(0, head)

    left_prev, cur = dummy, head
    for i in range(left - 1):
        left_prev, cur = cur, cur.next


    # now cur = left, left_prev = node before left
    prev = None
    for i in range(right - left + 1):
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp

    # update pointers
    left_prev.next.next = cur
    left_prev.next = prev
    return dummy.next

