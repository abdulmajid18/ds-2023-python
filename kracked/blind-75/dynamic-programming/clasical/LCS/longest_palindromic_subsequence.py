def longestCommonSubsequence(text1, text2):
    dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i][j + 1], dp[j][i + 1])
    return dp[0][0]


def longestPalindromeSubstring2(s):
    cache = {}

    def dfs(i, j):
        if i < 0 or j == len(s):
            return 0

        if (i, j) in cache:
            return cache[(i, j)]

        if s[i] == s[j]:
            length = 1 if i == j else 2
            cache[(i, j)] = length + dfs(i - 1, j + 1)

        else:
            cache[(i, j)] = max(dfs(i - 1, j), dfs(i, j - 1))

        return cache[(i, j)]

    for i in range(len(s)):
        dfs(i, i)  # odd length
        dfs(i, i + 1)  # even length


def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    # Initialize a 2D DP table with 0s
    dp = [[0] * n for _ in range(n)]

    # Base case: Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill the table for substrings of increasing length
    for length in range(2, n + 1):  # length of substring
        for i in range(n - length + 1):
            j = i + length - 1  # endpoint of the substring
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The result is stored in dp[0][n-1] (the whole string)
    return dp[0][n - 1]


def longestPalindromeSubseq2(s: str) -> int:
    n = len(s)
    rev_s = s[::-1]  # Reverse the string

    # Initialize a 2D DP table
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Fill the DP table using LCS logic
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == rev_s[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # The result is the LCS of s and rev_s
    return dp[n][n]


class Solution:
    def longestPalindromeSubseqdfs(self, s: str) -> int:
        n = len(s)

        # Use memoization to store results of subproblems
        memo = {}

        # Helper function to calculate the longest palindromic subsequence recursively
        def lps(left, right):
            # Base case: if the left index exceeds the right index
            if left > right:
                return 0
            # Base case: if left equals right, it's a single character
            if left == right:
                return 1

            # Check if the result is already computed
            if (left, right) in memo:
                return memo[(left, right)]

            # Case 1: Characters match
            if s[left] == s[right]:
                memo[(left, right)] = 2 + lps(left + 1, right - 1)
            else:
                # Case 2: Characters don't match
                memo[(left, right)] = max(lps(left + 1, right), lps(left, right - 1))

            return memo[(left, right)]

        # Start the recursion from the first and last characters
        return lps(0, n - 1)
