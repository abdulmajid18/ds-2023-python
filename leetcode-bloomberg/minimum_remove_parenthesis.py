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