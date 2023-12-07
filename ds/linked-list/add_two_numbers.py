class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        # Get values of the current nodes (if available)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate the sum and carry
        total_sum = val1 + val2 + carry
        carry = total_sum // 10
        digit = total_sum % 10

        # Create a new node with the calculated digit and move to the next node
        current.next = ListNode(digit)
        current = current.next

        # Move to the next nodes in the input lists (if available)
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next


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
        cur.next = ListNode(val)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


if __name__ == '__main__':
    ans = add_two_numbers(a, b)
    print(ans.val)
