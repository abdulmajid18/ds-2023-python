from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListBrute(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    vals = []
    while head:
        vals.append(head.val)
        head = head.next

    dummy = ListNode(0)
    curr = dummy
    for v in reversed(vals):
        curr.next = ListNode(v)
        curr = curr.next

    return dummy.next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head

    while curr:
        nxt = curr.next   # save next node
        curr.next = prev  # reverse the link
        prev = curr       # move prev forward
        curr = nxt        # move curr forward

    return prev
