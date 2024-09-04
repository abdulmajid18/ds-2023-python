def longestPalindromeBrute(self, s: str) -> str:
    def is_palindrome(s):
        return s == s[::-1]

    n = len(s)
    longest = ""

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j + 1]
            if is_palindrome(substring) and len(substring) > len(longest):
                longest = substring
    return longest


def longestPalindromeOptimalA(self, s: str) -> str:
    res = ""
    resLen = 0

    for i in range(len(s)):
        #  check odd length
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        # check en=ven length
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res
