def maxProfit(prices):
    if not prices:
        return 0

    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price

    return max_profit


from typing import List


def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0

    min_price = float('inf')  # Initialize min_price to infinity
    max_profit = 0  # Initialize max_profit to 0

    for price in prices:
        # Update min_price to be the minimum of the current min_price and the current price
        min_price = min(min_price, price)
        # Calculate the profit if we sold at the current price
        profit = price - min_price
        # Update max_profit to be the maximum of the current max_profit and the calculated profit
        max_profit = max(max_profit, profit)

    return max_profit
