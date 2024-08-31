from typing import List

"""
State Variables:

buy1: This variable keeps track of the maximum profit we can have after buying the first stock. Initially, 
this is set to negative infinity because we haven’t made any transaction yet, and we subtract the price from our cash 
balance. sold1: This represents the maximum profit after selling the first stock. We want this to be as high as 
possible because it gives us the profit from our first transaction. buy2: This is the maximum profit after buying the 
second stock. Here, we're working with the profit we made from the first sale, so buy2 is adjusted by subtracting the 
current price. sold2: Finally, this is the maximum profit after selling the second stock, which will give us the 
answer to the problem. State Transitions:

Every day, I update these variables based on the stock price:
buy1 = max(buy1, -price): Do I buy today, or keep my current state?
sold1 = max(sold1, buy1 + price): Do I sell today, or keep my current profit?
buy2 = max(buy2, sold1 - price): Do I use my profit from the first sale to buy again, or keep my current state?
sold2 = max(sold2, buy2 + price): Do I sell the second stock today, or hold onto it?
Why This Approach Works:

This approach is both time-efficient and space-efficient. It runs in O(n) time since we only loop through the prices once, updating our state variables in constant time. The space complexity is O(1) because we only use a fixed amount of extra space regardless of the input size.
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # Initialize state variables
        buy1, sold1 = float('-inf'), 0
        buy2, sold2 = float('-inf'), 0

        # Iterate through each price
        for price in prices:
            buy1 = max(buy1, -price)
            sold1 = max(sold1, buy1 + price)
            buy2 = max(buy2, sold1 - price)
            sold2 = max(sold2, buy2 + price)

        return sold2
