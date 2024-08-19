def search_range_brute_force(nums, target):
    first_occurrence = -1
    last_occurrence = -1

    # Finding the first occurrence
    for i in range(len(nums)):
        if nums[i] == target:
            first_occurrence = i
            break

    # Finding the last occurrence
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == target:
            last_occurrence = i
            break

    return [first_occurrence, last_occurrence]


# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = search_range_brute_force(nums, target)
print(f"The first and last position of {target} in the array are: {result}")
