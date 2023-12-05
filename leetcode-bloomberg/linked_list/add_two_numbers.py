class ListNode:
    def __int__(self, val=0, next=None):
        self.val = val
        self.next = next


a = ListNode()
a.val = 2
b = ListNode()
b.val = 3



def add_two_numbers(l1: ListNode, l2: ListNode):
    dummy = ListNode()
    cur = dummy

    carry = 0
    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        val = v1 + v2 + carry
        carry = val // 10
        val = val % 10
        cur.next = ListNode().val = val

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


if __name__ == '__main__':
    ans = add_two_numbers(a, b)
    print(ans.val)