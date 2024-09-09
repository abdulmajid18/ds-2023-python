class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
Explanation:
Two Pointers (pA and pB):

pA starts at headA and pB starts at headB. As we traverse through the lists, if pA reaches the end of list A, 
we reset it to the head of list B, and similarly, if pB reaches the end of list B, we reset it to the head of list A. 
Synchronization:

By resetting each pointer when it reaches the end of its list, we ensure that both pointers will eventually traverse the same number of nodes. After at most two passes through the lists, the two pointers will either meet at the intersection or both reach None, indicating no intersection.
Termination:

The loop exits when pA == pB. If both are None, there is no intersection. Otherwise, pA and pB will point to the intersection node.
Time and Space Complexity:
Time Complexity: O(n + m), where n is the length of list A and m is the length of list B. In the worst case, both pointers will traverse both lists once.
"""


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
