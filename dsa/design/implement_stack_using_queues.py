from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

    def pop(self):
        for i in range(len(self.q) - 1):
            val = self.q.popleft()
            self.q.append(val)
        return self.q.popleft()

    def top(self):
        return self.q[-1]

    def empty(self):
        return len(self.q) == 0
