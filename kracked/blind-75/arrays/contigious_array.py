def findMaxLengthBruteForce(nums):
    max_length = 0
    n = len(nums)

    for i in range(n):
        count_0 = 0
        count_1 = 0
        for j in range(i, n):
            # Count 0's and 1's in the current subarray
            if nums[j] == 0:
                count_0 += 1
            else:
                count_1 += 1

            # If the counts are equal, update the maximum length
            if count_0 == count_1:
                max_length = max(max_length, j - i + 1)

    return max_length


def findMaxLength(nums):
    # HashMap to store the first occurrence of each cumulative sum
    sum_index_map = {0: -1}  # Initialize with cumulative sum 0 at index -1
    max_length = 0
    cumulative_sum = 0

    for i, num in enumerate(nums):
        # Convert 0 to -1
        cumulative_sum += -1 if num == 0 else 1

        if cumulative_sum in sum_index_map:
            # If cumulative sum has been seen before, calculate the length
            max_length = max(max_length, i - sum_index_map[cumulative_sum])
        else:
            # Store the first occurrence of this cumulative sum
            sum_index_map[cumulative_sum] = i

    return max_length
