class SolutionBrute:
    def reverseWords(self, s: str) -> str:
        stack = []
        words = s.split()

        for word in words:
            stack.append(word)

        res = []
        while stack:
            res.append(stack.pop())

        return " ".join(res)


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()  # Remove extra spaces and split into words
        left, right = 0, len(words) - 1

        # Swap words using two pointers
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        return " ".join(words)  # Rejoin words with a single space
