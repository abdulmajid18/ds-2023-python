class SolutionBrute:
    def isPalindrome(self, s: str) -> bool:
        # Filter the string to keep only alphanumeric characters and convert to lowercase
        filtered_chars = [c.lower() for c in s if c.isalnum()]

        # Initialize a stack and push all the filtered characters onto it
        stack = []
        for char in filtered_chars:
            stack.append(char)

        # Iterate over the filtered characters and compare with the stack's top element
        for char in filtered_chars:
            if char != stack.pop():
                return False

        return True



class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1  # Initialize pointers at both ends

        while l < r:
            # Skip non-alphanumeric characters
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            # Compare characters in a case-insensitive manner
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True  # If all characters match, it's a palindrome

