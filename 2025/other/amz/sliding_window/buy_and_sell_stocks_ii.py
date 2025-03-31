from typing import List


def maxProfitBruteForce(prices):
    n = len(prices)
    max_profit = 0

    for i in range(n):  # Buy day
        for j in range(i + 1, n):  # Sell day
            if prices[j] > prices[i]:  # Only count profitable transactions
                max_profit += prices[j] - prices[i]

    return max_profit


# Example usage:
prices = [7, 1, 5, 3, 6, 4]
print(maxProfitBruteForce(prices))  # Output: Incorrect (Overcounts)


class SolutionOptimal:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for r in range(1, len(prices)):
            if prices[r] > prices[r-1]:
                profit += (prices[r] - prices[r - 1])
        return profit
