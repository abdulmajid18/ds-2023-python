class Solution:
    def divisorGame(self, n: int) -> bool:
        return n % 2 == 0


def divisorGame(N):
    dp = [False] * (N + 1)  # Initialize the DP array, size N+1

    # Base case: dp[1] is False because you lose if you start with 1
    dp[1] = False

    # Start from number 2 to N, and calculate dp[i] for each number
    for i in range(2, N + 1):
        for j in range(1, i):
            if i % j == 0 and not dp[i - j]:  # Check if dp[i-j] is False (losing state)
                dp[i] = True  # Mark dp[i] as True, meaning the current player can win
                break  # No need to check further, we found a winning move

    # Return the result for dp[N] (whether the starting player wins with N)
    return dp[N]

