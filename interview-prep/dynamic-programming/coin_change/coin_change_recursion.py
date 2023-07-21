import sys

class CoinChangeRecursion:
    def coin_change(self, coins, amount):
        value = [amount + 1] * (amount + 1)
        value[0] = 0

        for x in range(1, amount + 1):
            for i, coin in enumerate(coins):
                if x - coin >= 0:
                    value[x] = min(value[x], value[x-coin] + 1)
        return value[amount] if value[amount] != amount + 1 else -1
