from typing import List

"""Approach: Greedy The optimal strategy for this problem is a greedy approach. This approach involves buying when 
the price is going to increase in the future and selling when it’s going to decrease. Essentially, you should capture 
all upward trends in the stock price."""

def maxProfit(prices: List[int]) -> int:
    total_profit = 0
    n = len(prices)

    # Iterate through the list of prices
    for i in range(1, n):
        # If today's price is less than tomorrow's price, we can make a profit
        if prices[i] > prices[i - 1]:
            # Buy at prices[i - 1] and sell at prices[i]
            total_profit += prices[i] - prices[i - 1]

    return total_profit
