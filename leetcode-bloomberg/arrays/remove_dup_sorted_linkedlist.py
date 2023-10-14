from data_structures.node.nodde import LinkedList


def remove_dup_sorted(l: LinkedList):
    cur = l.head

    while cur:
        while cur.next and cur.next.data == cur.data:
            cur.next = cur.next.next
        cur = cur.next
    return l.head
