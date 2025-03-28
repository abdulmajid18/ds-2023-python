from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # Define vowel set
        s = list(s)  # Convert string to a list for modification
        l, r = 0, len(s) - 1  # Two pointers

        while l < r:
            # Move left pointer until it finds a vowel
            while l < r and s[l] not in vowels:
                l += 1
            # Move right pointer until it finds a vowel
            while l < r and s[r] not in vowels:
                r -= 1

            # Swap vowels at l and r
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)  # Convert list back to string


class Solution:
    def reverseWords(self, s: str) -> str:
        # Convert string to a list of characters (since Python strings are immutable)
        chars = list(s.strip())  # Remove leading/trailing spaces

        # Step 1: Reverse the entire string
        self.reverse(chars, 0, len(chars) - 1)

        # Step 2: Reverse each word in-place
        n = len(chars)
        left = 0
        while left < n:
            # Find the end of the current word
            right = left
            while right < n and chars[right] != ' ':
                right += 1
            # Reverse the current word
            self.reverse(chars, left, right - 1)
            # Move left to the start of the next word
            left = right + 1

        # Step 3: Remove extra spaces and join
        return " ".join("".join(chars).split())

    def reverse(self, chars, left, right):
        """Helper function to reverse a part of the list in-place."""
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
