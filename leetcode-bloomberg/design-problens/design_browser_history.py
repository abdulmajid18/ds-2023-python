class ListNode:
    def __int__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowsingHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self,url: str):
        new_node = ListNode(url, prev=self.cur)
        self.cur.next = new_node
        self.cur = self.cur.next

    def back(self, steps):
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def back(self, steps):
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 0
        return self.cur.val

class BrowsingHistoryArrayStack:
    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]

    def visit(self,url: str):
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1

    def back(self, steps):
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    def back(self, steps):
        self.i = min(self.i + steps, self.len - 1)
        return self.history[self.i]