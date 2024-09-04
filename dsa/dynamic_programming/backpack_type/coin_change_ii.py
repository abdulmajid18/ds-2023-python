def change(amount, coins):
    # Initialize a list to hold the number of ways to make each amount
    dp = [0] * (amount + 1)
    # There's one way to make amount 0: use no coins
    dp[0] = 1

    # Iterate over each coin
    for coin in coins:
        # For each amount from the coin's value to the target amount
        for c in range(coin, amount + 1):
            # Update the number of ways to make the current amount
            dp[c] += dp[c - coin]
        print(dp)

    # Return the number of ways to make the target amount
    return dp[amount]


amount = 5
coins = [1,2]


ans = change(amount, coins)
print(ans)