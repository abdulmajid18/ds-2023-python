from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1  # Two-pointer approach

        while l < r:
            s[l], s[r] = s[r], s[l]  # Swap elements
            l += 1  # Move left pointer forward
            r -= 1  # Move right pointer backward
