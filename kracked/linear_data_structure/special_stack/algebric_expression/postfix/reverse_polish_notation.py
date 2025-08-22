from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}

        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                nums2 = stack.pop()
                nums1 = stack.pop()

                if s == "+":
                    res = nums1 + nums2

                elif s == "-":
                    res = nums1 - nums2

                elif s == "*":
                    res = nums1 * nums2
                else:
                    res = int(nums1 / nums2)

                stack.append(res)
        return stack[-1]

