from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)

        # Initialize the states
        hold = -float('inf')  # Maximum profit when holding a stock
        sold = 0  # Maximum profit after selling a stock
        sold_cd = 0  # Maximum profit in cooldown

        for price in prices:
            prev_sold = sold

            # Update the states
            hold = max(hold, sold_cd - price)
            sold = max(sold, hold + price)
            sold_cd = prev_sold

        return sold
