from collections import deque


class MyStack:

    def __init__(self):
        self.q1 = deque()  # Main queue
        self.q2 = deque()  # Temporary queue

    def push(self, x: int) -> None:
        # Always push to the temporary queue first
        self.q2.append(x)

        # Move all elements from q1 to q2, so that the last pushed element is in front
        while self.q1:
            self.q2.append(self.q1.popleft())

        # Swap the names of q1 and q2 to maintain stack order
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # Pop from q1, which simulates stack behavior
        return self.q1.popleft()

    def top(self) -> int:
        # Peek the front element of q1
        return self.q1[0]

    def empty(self) -> bool:
        # Check if q1 is empty
        return len(self.q1) == 0
