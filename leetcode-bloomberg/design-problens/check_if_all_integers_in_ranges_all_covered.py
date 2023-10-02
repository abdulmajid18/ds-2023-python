def isCovered(ranges, left, right):
    # Initialize a list to represent the prefix sum of covered intervals.
    prefix_sum = [0] * (52)  # Using 52 to handle the range [-50, 50].

    # Mark the start and end points of each interval in the prefix sum array.
    for start, end in ranges:
        prefix_sum[start] += 1
        prefix_sum[end + 1] -= 1

    # Calculate the prefix sum.
    current_sum = 0
    for i in range(52):
        current_sum += prefix_sum[i]
        # If we encounter any position with a prefix sum of 0 and it's within [left, right], return False.
        if left <= i <= right and current_sum == 0:
            return False

    return True


def isCoveredBruteForce(ranges, left, right):
    for num in range(left, right + 1):
        is_covered = False
        for start, end in ranges:
            if start <= num <= end:
                is_covered = True
                break
        if not is_covered:
            return False
    return True
