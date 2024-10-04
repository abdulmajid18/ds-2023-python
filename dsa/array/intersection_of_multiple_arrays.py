from collections import defaultdict


def intersection(nums):
    count_map = defaultdict(int)
    num_arrays = len(nums)

    # Count occurrences of each number
    for array in nums:
        unique_elements = set(array)  # To avoid counting duplicates in the same array
        for num in unique_elements:
            count_map[num] += 1

    # Collect elements that are present in all arrays
    result = [num for num, count in count_map.items() if count == num_arrays]

    return result


# Example usage
nums = [[3, 1, 2, 4], [2, 4, 3], [4, 3]]
result = intersection(nums)
print(result)  # Output: [3, 4]
