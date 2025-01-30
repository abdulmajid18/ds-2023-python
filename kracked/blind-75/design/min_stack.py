class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        # If stack is empty, push (x, x) where x is the element and also the minimum
        if not self.stack:
            self.stack.append((x, x))
        else:
            # If the stack is not empty, compare the current value with the min value on top of the stack
            current_min = self.stack[-1][1]
            self.stack.append((x, min(x, current_min)))

    def pop(self) -> None:
        # Pop the top of the stack (element, min value)
        self.stack.pop()

    def top(self) -> int:
        # Return the top element (the first value in the tuple)
        return self.stack[-1][0]

    def getMin(self) -> int:
        # Return the minimum value (the second value in the tuple)
        return self.stack[-1][1]


class MinStack2:
    def __init__(self):
        self.stack = []  # The main stack for storing elements.
        self.min_stack = []  # The stack for tracking the minimum element.

    def push(self, x: int) -> None:
        # Push the element onto the main stack.
        self.stack.append(x)
        val = min(x, self.min_stack[-1] if self.min_stack else x)
        self.min_stack.append(val)

    def pop(self) -> None:
        # Pop the element from the main stack.
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        # Return the top element of the main stack.
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        # Return the top element of the min_stack, which is the minimum element.
        return self.min_stack[-1] if self.min_stack else None
