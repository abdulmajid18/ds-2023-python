from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    maxProfit = 0

    for r in range(1, len(prices)):
        profit = prices[r] - min_price
        maxProfit = max(maxProfit, profit)

        min_price = min(min_price, prices[r])

    return maxProfit