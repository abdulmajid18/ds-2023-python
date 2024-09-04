def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    # Create a 2D dp array with n x n dimensions initialized to 0
    dp = [[0] * n for _ in range(n)]

    # Base case: single letter palindromes
    for i in range(n):
        dp[i][i] = 1

    # Build the dp table
    for length in range(2, n + 1):  # length of the current substring
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # The answer is the maximum palindromic subsequence length for the whole string
    return dp[0][n - 1]

# Example usage
s = "bbbab"
print(longestPalindromeSubseq(s))  # Output: 4
