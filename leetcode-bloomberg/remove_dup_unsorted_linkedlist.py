from data_structures.node.nodde import LinkedList


def remove_dup(l: LinkedList):
    current = l.head
    previous = None
    seen = set()

    while current:
        if current.data in seen:
            previous.next = current.next
        else:
            seen.add(current.data)
            previous = current
        current = current.next

    l.tail = previous
    return l


def remove_dup_followup(l: LinkedList):
    runner = l.head
    current = l.head

    while current:
        runner = current
        while runner.next:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    l.tail = runner
    return l


def remove_dup_sorted(l: LinkedList):
    cur = l.head

    while cur:
        while cur.next and cur.next.data == cur.data:
            cur.next = cur.next.next
        cur = cur.next
    return l.head
