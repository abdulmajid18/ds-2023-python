class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        i, j = len(text1), len(text2)

        dp = [[0] * (j + 1) for _ in range(i + 1)]

        for m in range(1, i + 1):
            for n in range(1, j + 1):
                if text1[m - 1] == text2[n - 1]:
                    dp[m][n] = 1 + dp[m - 1][n - 1]
                else:
                    dp[m][n] = max(dp[m - 1][n], dp[m][n - 1])

        return dp[i][j]
