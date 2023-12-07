def maxDepth(s):
    max_depth = 0  # Initialize the maximum depth to 0
    current_depth = 0  # Initialize the current depth to 0

    for char in s:
        if char == '(':
            current_depth += 1  # Increment the depth when an opening parenthesis is encountered
            max_depth = max(max_depth, current_depth)  # Update the maximum depth if needed
        elif char == ')':
            current_depth -= 1  # Decrement the depth when a closing parenthesis is encountered
            if current_depth < 0:
                return -1  # If the depth becomes negative, the parentheses are not balanced

    # Check if parentheses are balanced (current_depth should be 0 at the end)
    return max_depth if current_depth == 0 else -1

# Example usage:
s = "(a(b(c)d)e)"
result = maxDepth(s)
print(result)  # Output: 3 (maximum depth of nested parentheses is 3)


def maxDepthStack(s):
    max_depth = 0
    current_depth = 0
    stack = []

    for char in s:
        if char == '(':
            stack.append(char)
            current_depth = len(stack)
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            if not stack:
                return -1  # Unbalanced closing parenthesis
            stack.pop()

    if stack:
        return -1  # Unbalanced opening parenthesis

    return max_depth