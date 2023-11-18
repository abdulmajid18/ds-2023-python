from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        # Enqueue the new element to queue1
        self.queue1.append(x)

        # Move all elements from queue2 to queue1
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

        # Swap the names of queue1 and queue2
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        # Pop the front element from queue2
        if self.queue2:
            return self.queue2.popleft()

    def top(self):
        # Return the front element of queue2 without dequeuing
        if self.queue2:
            return self.queue2[0]

    def empty(self):
        # Check if both queues are empty
        return not self.queue2
