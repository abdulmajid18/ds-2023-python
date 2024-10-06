def twoSum(nums, target):
    # Loop through each element in the list
    for i in range(len(nums)):
        # For each element, loop through the rest of the elements
        for j in range(i + 1, len(nums)):
            # If the sum of nums[i] and nums[j] equals the target, return their indices
            if nums[i] + nums[j] == target:
                return [i, j]
    return None  # Return None if no solution is found


def twoSum2(nums, target):
    for i, v1 in enumerate(nums):
        for j, v2 in enumerate(nums):
            # Skip if comparing the same element
            if i == j:
                continue
            elif v1 + v2 == target:
                return i, j  # Return indices, not values
    return None


def twoSumHashMap(nums, target):
    table = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in table:
            return i, table[complement]
        table[n] = i
