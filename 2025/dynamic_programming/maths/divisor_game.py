class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0


def divisorGame(N):
    dp = [False] * (N + 1)

    for i in range(2, N + 1):
        for j in range(1, i):
            if i % j == 0 and not dp[i - j]:
                dp[i] = True
                break

    return dp[N]
