class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for element in s:
            if stack and stack[-1][0] == element:
                stack[-1][1] += 1
            else:
                stack.append([element, 1])
            if stack[-1][1] == k:
                stack.pop()

        res = ''
        for i in stack:
            elements = i[0] * i[1]
            res += elements

        return res
