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
