def buy_sell(prices):
    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > profit[i - 1]:
            profit += prices[i] - prices[i - 1]

    return profit
