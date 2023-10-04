
class Node2:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        self.child = None

def flatten(head: Node2):
    if not head:
        return head

    dummy = Node2(0)
    cur, stack = dummy, [head]
    while cur:
        temp = stack.pop()
        if temp.next:
            stack.append(temp.next)
        if temp.child:
            stack.append(temp.child)
        cur.next = temp
        temp.prev = cur
        temp.child = None
        cur = temp
    dummy.next.prev = None
    return dummy.next

