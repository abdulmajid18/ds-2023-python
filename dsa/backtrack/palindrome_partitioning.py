from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []  # Final list to store all palindrome partitions
        part = []  # Temporary list to store current partition

        # DFS function to explore all partitions
        def dfs(start):
            if start >= len(s):  # If we have reached the end of the string
                res.append(part.copy())  # Add the current partition to the result
                return

            # Explore all substrings starting from 'start'
            for end in range(start, len(s)):
                if self.isPali(s, start, end):  # If the substring s[start:end+1] is a palindrome
                    part.append(s[start:end + 1])  # Add the palindrome substring to the current partition
                    dfs(end + 1)  # Recurse for the remaining part of the string
                    part.pop()  # Backtrack and remove the last palindrome substring

        dfs(0)  # Start DFS from the first character
        return res

    # Helper function to check if a substring is a palindrome
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

