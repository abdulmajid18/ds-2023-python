def isValid(self, s: str) -> bool:
    stack = []
    parentheses = {')': '(', ']': '[', '}': '{'}

    for p in s:
        if p in parentheses:
            if stack and stack[-1] == parentheses[p]:
                stack.pop()
            else:
                return False
        else:
            stack.append(p)

    return True if not stack else False