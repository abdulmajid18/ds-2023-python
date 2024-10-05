class MyQueue:

    def __int__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s2.pop())
        return self.s2.pop()

    def peek(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s2.pop())
        return self.s2[-1]

    def empty(self):
        return max(len(self.s2), len(self.s1))
