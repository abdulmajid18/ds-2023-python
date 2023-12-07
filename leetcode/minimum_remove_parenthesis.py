def minimum_remove(s):
    stack = []
    S = list(s)
    N = len(s)

    for i in range(N):
        if S[i] == '(':
            stack.append(i)
        elif S[i] == ')':
            if stack:
                stack.pop()
            else:
                S[i] = ''

    for j in stack:
        S[j] = ''

    return ''.join(stack)


def minRemoveToMakeValid(s):
    stack = []
    removals = set()

    # Step 1: Find unmatched open parentheses and mark for removal.
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                removals.add(i)

    # Mark unmatched open parentheses for removal.
    removals.update(stack)

    # Step 2: Create the modified string without marked characters.
    result = []
    for i, char in enumerate(s):
        if i not in removals:
            result.append(char)

    return ''.join(result)

# Example usage:
s = "lee(t(c)o)de)"
print(minRemoveToMakeValid(s))  # Output: "lee(t(c)o)de"
