class Solution1:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution2:
    def climbStairs(self, n: int, memo=None) -> int:
        # Initialize memo dictionary if not provided
        if memo is None:
            memo = {}

        # Base cases
        if n == 0 or n == 1:
            return 1

        # Check if the result is already in memo
        if n in memo:
            return memo[n]

        # Compute the result and store it in memo
        memo[n] = self.climbStairs(n - 1, memo) + self.climbStairs(n - 2, memo)

        # Return the result
        return memo[n]


# Example usage:
solution = Solution2()
n = 5
print(f"Number of ways to climb {n} stairs: {solution.climbStairs(n)}")


class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n - 1] = 1

        for i in range(n - 2, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]

        return dp[0]
