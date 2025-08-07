def climbStairs(n: int) -> int:

    def climb(n):
        if n <= 2:
            return n
        if n in memo:
            return memo[n]
        memo[n] = (climb(n - 1) + climb(n - 2))
        return memo[n]

    memo = {}

    return climb(n)


def climbStairsTwo(n: int) -> int:
    if n <= 2:
        return n

    first, second = 1, 2
    for i in range(3, n + 1):
        third = first + second
        first = second
        second = third
    return second


def climbStairsDP(n: int) -> int:
    if n <= 2:
        return n

    dp = [0] * (n + 1)
    dp[0] = 1  # 1 way to be at step 0 (do nothing)
    dp[1] = 1  # 1 way to reach step 1 (0 → 1)

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
