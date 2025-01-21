def longest_valid_parentheses(s):
    stack = [-1]
    max_length = 0

    for i, char in enumerate(s):
        if char == "(":
            stack.append(i)
        else:
            left_par_idx = stack.pop()
            if not stack:
                stack.append(i)
            else:
                max_length = max(max_length, i - left_par_idx)
    return max_length


# a = "(()"

def longestValidParenthesesTwoPass(s: str) -> int:
    # Using two passes
    max_length = 0
    open_count, close_count = 0, 0

    # Left to right
    for char in s:
        if char == '(':
            open_count += 1
        else:
            close_count += 1
        if open_count == close_count:
            max_length = max(max_length, 2 * close_count)
        elif close_count > open_count:
            open_count = close_count = 0

    # Right to left
    open_count, close_count = 0, 0
    for char in reversed(s):
        if char == '(':
            open_count += 1
        else:
            close_count += 1
        if open_count == close_count:
            max_length = max(max_length, 2 * open_count)
        elif open_count > close_count:
            open_count = close_count = 0

    return max_length
