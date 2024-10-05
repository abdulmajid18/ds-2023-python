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


def intersection2(nums):
    if not nums:
        return []

    # Use a dictionary to count occurrences of elements in the first array
    count = {}
    for num in nums[0]:
        count[num] = 1

    # Iterate through the other arrays and update the count
    for array in nums[1:]:
        # Use a temporary set to track which elements are seen in the current array
        seen = set(array)
        # Update the count dictionary
        for key in list(count.keys()):
            if key not in seen:
                del count[key]

    # The result is the keys that are present in the count dictionary
    return list(count.keys())

# Example usage
nums = [[3, 1, 2, 4], [2, 4, 3], [4, 3]]
result = intersection(nums)
print(result)  # Output: [3, 4]


# Example usage
nums = [[3, 1, 2, 4], [2, 4, 3], [4, 3]]
result = intersection(nums)
print(result)  # Output: [3, 4]
