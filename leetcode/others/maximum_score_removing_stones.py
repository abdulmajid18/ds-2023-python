def maximumScore(a, b, c):
    # Sort the pile sizes in descending order
    pile_sizes = sorted([a, b, c], reverse=True)

    # Calculate the maximum score
    max_score = 0

    while pile_sizes[1] > 0:
        # Take one stone from the two largest piles

        pile_sizes[0] -= 1
        pile_sizes[1] -= 1

        max_score += 1

        # Re-sort the pile sizes
        pile_sizes.sort(reverse=True)

    return max_score

# Example usage:
a = 2
b = 4
c = 6
result = maximumScore(a, b, c)
print("Maximum score:", result)  # Output: Maximum score: 6
