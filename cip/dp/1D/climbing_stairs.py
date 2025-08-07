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