class Solution:
    def coin_change_dp(self, coins: list[int], amount: int):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1

    def coin_change_recursion(self, coins, amount):
        # handle payment amount
        if not amount:
            return []
        if amount < 0:
            return None
        optimal_result = None
        for coin in coins:
            partial_result = self.coin_change_recursion(coins, amount - coin)
            if partial_result is None:
                continue
            candidate = partial_result + [coin]
            if (optimal_result is None or
                    len(candidate) < len(optimal_result)):
                optimal_result = candidate
        return optimal_result

    def coin_change_bottom_up(self, coins, amount):
        solulions = [None] * (amount + 1)
        solulions[0] = []

        paid = 0
        while paid < amount:
            if solulions[paid] is not None:
                for coin in coins:
                    next_paid = paid + coin
                    if next_paid > amount:
                        continue
                    if (solulions[next_paid] is None or
                        len(solulions[next_paid]) > len(solulions[paid]) + 1):
                        solulions[next_paid] = solulions[paid] + coin
            paid += 1
        return solulions[amount]





def main():
    coins = [1, 2, 5]
    amount = 9
    solution = Solution()
    answer = solution.coin_change_recursion(coins, amount)
    print(answer)


if __name__ == '__main__':
    main()
