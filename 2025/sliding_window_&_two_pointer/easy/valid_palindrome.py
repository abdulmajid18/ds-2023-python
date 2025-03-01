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
