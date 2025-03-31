from typing import List

class SolutionDP:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, buy2 = float("inf"), float("inf")
        sell1, sell2 = 0, 0

        for price in prices:
            buy1 = min(buy1, price)  # Best price to buy first stock
            sell1 = max(sell1, price - buy1)  # Max profit from first sell
            buy2 = min(buy2, price - sell1)  # Best price to buy second stock (accounting for first profit)
            sell2 = max(sell2, price - buy2)  # Max profit from second sell

        return sell2

# Example
prices = [3,3,5,0,0,3,1,4]
sol = SolutionDP()
print(sol.maxProfit(prices))  # Output: 6
