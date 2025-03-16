class Solution:
    def numDecodings(self, s: str) -> int:
        def dfs(i):
            # Base case: If we reach the end of the string, count this as 1 way
            if i == len(s):
                return 1
            # If the current digit is '0', we can't decode it
            if s[i] == '0':
                return 0

            # Decode single character
            res = dfs(i + 1)

            # Decode two characters if valid
            if i + 1 < len(s) and '10' <= s[i:i + 2] <= '26':
                res += dfs(i + 2)

            return res

        return dfs(0)


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == '0':
                return 0

            res = dfs(i + 1)

            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456"):
                res += dfs(i + 2)

            dp[i] = res
            return res

        return dfs(0)