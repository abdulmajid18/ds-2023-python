class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        # dp[i] will store the number of ways to reach the i-th step from the top (step n)
        dp = [0] * (n + 1)

        # Base cases
        dp[n] = 1  # 1 way to stay on step n (do nothing)
        dp[n - 1] = 1  # 1 way to go from step n-1 to step n (one step forward)

        # Fill the dp array from the top down to step 0
        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        # The answer is the number of ways to get from step 0 to step n
        return dp[0]
