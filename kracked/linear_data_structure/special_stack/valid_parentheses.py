class Solution:
    def isValid(self, s: str) -> bool:
        close = {")": "(", "}": "{", "]": "["}

        stack = []

        for bracket in s:
            if bracket not in close:
                stack.append(bracket)
            else:
                if not stack or stack.pop() != close[bracket]:
                    return False
        return not stack

