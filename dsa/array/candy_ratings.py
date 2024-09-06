def candy(ratings):
    n = len(ratings)
    # Initialize the candies array with 1 candy for each child
    candies = [1] * n

    # First pass: left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Second pass: right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    # Return the total number of candies
    return sum(candies)


# Example usage
ratings = [1, 0, 2]
print(candy(ratings))  # Output: 5
