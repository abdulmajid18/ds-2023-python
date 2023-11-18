def isValid(s):
    stack = []
    # Define a mapping of opening and closing parentheses
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        # If the character is a closing parenthesis
        if char in mapping:
            # Pop the top element from the stack if it is not empty; otherwise, use a dummy value '#'
            top_element = stack.pop() if stack else '#'

            # Check if the popped element matches the corresponding opening parenthesis
            if mapping[char] != top_element:
                return False
        else:
            # If it's an opening parenthesis, push it onto the stack
            stack.append(char)

    # The string is valid if the stack is empty at the end
    return not stack


# Example usage:
print(isValid("()"))  # Output: True
print(isValid("()[]{}"))  # Output: True
print(isValid("(]"))  # Output: False
print(isValid("([)]"))  # Output: False
print(isValid("{[]}"))  # Output: True
