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
