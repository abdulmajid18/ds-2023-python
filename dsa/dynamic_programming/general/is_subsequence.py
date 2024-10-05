class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        if i < len(s):
            return False
        else:
            return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # Pointer for s
        j = 0  # Pointer for t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # Compare characters from s and t
                i += 1  # Move pointer in s
            j += 1  # Always move pointer in t

        return i == len(s)  # If i reaches the end of s, it means all characters of s are found in t
