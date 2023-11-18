class MinStack:
    def __init__(self):
        # The main stack to store elements
        self.stack = []
        # The auxiliary stack to keep track of the minimum element at each step
        self.min_stack = []

    def push(self, x):
        # Push the element onto the main stack
        self.stack.append(x)

        # Update the minimum element in the auxiliary stack
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        # Pop the top element from the main stack
        if self.stack:
            # If the popped element is the current minimum, update the minimum stack
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            self.stack.pop()

    def top(self):
        # Return the top element of the main stack
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        # Return the minimum element from the auxiliary stack
        if self.min_stack:
            return self.min_stack[-1]


# Example usage:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)

print(minStack.getMin())  # Output: -3
minStack.pop()
print(minStack.top())  # Output: 0
print(minStack.getMin())  # Output: -2
