class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    # Initialize two pointers
    pA, pB = headA, headB

    # Traverse through both lists
    while pA != pB:
        # If pA reaches the end of list A, jump to the head of list B
        pA = pA.next if pA else headB
        # If pB reaches the end of list B, jump to the head of list A
        pB = pB.next if pB else headA

    # Either pA == pB (intersection) or both are None (no intersection)
    return pA
