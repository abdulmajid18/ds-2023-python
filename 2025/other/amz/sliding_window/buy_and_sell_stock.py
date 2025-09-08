from typing import List


class SolutionBruteForce:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        for i in range(n):
            for j in range(i + 1, n):  # Buy at i, sell at j
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)

        return max_profit


# Example Usage
prices = [7, 1, 5, 3, 6, 4]
solBrute = SolutionBruteForce()
print(solBrute.maxProfit(prices))  # Output: 5


class SolutionOptimal:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1

        return maxProfit


class SolutionOptimalTwo:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0  # Left pointer (buy day)
        maxProfit = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r

        return maxProfit


# Example Usage
prices = [7, 1, 5, 3, 6, 4]
sol = SolutionOptimalTwo()
print(sol.maxProfit(prices))  # Output: 5


class SolutionTwo:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        maxProfit = 0

        for r in range(1, len(prices)):
            profit = prices[r] - min_price
            maxProfit = max(maxProfit, profit)

            min_price = min(min_price, prices[r])

        return maxProfit


# Example Usage
prices = [7, 1, 5, 3, 6, 4]
sol = Solution()
print(maxProfit(prices))  # Output: 5
