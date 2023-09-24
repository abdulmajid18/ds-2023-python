class Node:

    def __int__(self, data=None, next_node: 'Node' = None):
        self.data = data
        self.next = next_node

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def has_next(self):
        return self.next is not None


class LinkedList(object):
    def __int__(self, node: Node = None):
        self.length = 0
        self.head = node
        self.tail = None

    def length(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count

    def insert_at_beginning(self, data):
        new_node = Node()
        new_node.data = data
        if self.length == 0:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert_at_end(self, data):
        new_node = Node()
        new_node.data = data
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        self.length += 1

    def insert_at_a_given_position(self, pos, data):
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0:
                self.insert_at_beginning(data)
            else:
                if pos == self.length:
                    self.insert_at_end(data)
                else:
                    new_node = Node()
                    new_node.data = data
                    count = 1
                    current = self.head
                    while count < pos - 1:
                        count += 1
                        current = current.next
                    new_node.next = current.next
                    current.next = new_node
                    self.length += 1

    def delete_from_beginning(self):
        if self.length == 0:
            print("This list is Empty")
        else:
            self.head = self.head.next
            self.length -= 1

    def delete_last_node(self):
        if self.length == 0:
            print("This list is Empty")
        else:
            current_node = self.head
            previous_node = self.head
            while current_node.next is not None:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = Node
            self.length -= 1
