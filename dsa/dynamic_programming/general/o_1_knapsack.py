def knapsack(weights, values, W):
    n = len(weights)
    # Create a DP table with all values initialized to 0
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    # Build the table in bottom-up manner
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                # Max of including or not including the current item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Can't include the item as it exceeds the current capacity
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]


# Example usage
weights = [1, 2, 3, 2]
values = [8, 4, 0, 5]
W = 5
print(knapsack(weights, values, W))  # Output should be the maximum value that can be obtained
