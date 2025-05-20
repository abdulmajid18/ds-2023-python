class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        for i in range(m):
            needle_substring = haystack[i: i + n]
            if needle_substring == needle:
                return i
        return -1


def strStr2(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)

    for i in range(n - m + 1):
        if haystack[i:i + m] == needle:
            return i
    return -1
