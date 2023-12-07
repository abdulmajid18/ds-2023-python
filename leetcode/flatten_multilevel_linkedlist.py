from __future__ import annotations

"""Problem Description
Imagine a linked list with not just a next node, but a down node as well. We want to write a function that would "Flatten" that linked list by taking all the downward segments and merging them up between their parent and their parent's next.

Sample inputs - Expected outputs"""


class Node2:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.child = None


def flattenListactual(head):
    headcop = head
    save = [head]
    # we could use a dummy here
    # dummy = Node()
    # prev = dummy
    prev = None

    while len(save) != 0:
        temp = save[-1]
        save.pop()

        if temp.next:
            save.append(temp.next)
        if temp.down:
            save.append(temp.down)

        if prev is not None:
            prev.next = temp

        # if there is a dummy

        prev = temp

    return headcop


# Python3 program to flatten a multilevel
# linked list

# A Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.down = None
        self.Next = None


last = None


# Flattens a multi-level linked
# list depth wise
def flattenList(node):
    if node is None:
        return None

    # To keep track of last visited
    # node
    # (NOTE: This is )
    last = node

    # Store next pointer
    Next = node.Next

    # If down list exists, process it
    # first. Add down list as next of
    # current node
    if node.down is not None:
        node.Next = flattenList(node.down)

    # If next exists, add it after the
    # next of last added node
    if Next is not None:
        last.Next = flattenList(Next)

    return node
