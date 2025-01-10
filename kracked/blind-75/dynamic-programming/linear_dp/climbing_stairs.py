def climbStairs(n: int) -> int:
    if n == 1:
        return 1

    # DP array to store the number of ways to reach each step
    dp = [0] * (n + 1)

    # Base cases
    dp[0] = 1  # 1 way to stay at the ground (step 0)
    dp[1] = 1  # 1 way to reach the first step

    # Fill the DP array for steps 2 to n
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    # The answer is the number of ways to reach step n
    return dp[n]
