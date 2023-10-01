class ListNode:
    def __int__(self, data, next_node=None):
        self.data = data
        self.next = next_node


def search_list(L: ListNode, key):
    while L and L.data != key:
        L = L.next
    return L


def insert_after(node: ListNode, new_node: ListNode):
    new_node.next = node.next
    node.next = new_node


def delete_after(node):
    node.next = node.next.next
