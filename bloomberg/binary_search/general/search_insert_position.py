def search_insert(nums, target):
    # Iterate through the array
    for i in range(len(nums)):
        # If target is found or a larger element is found, return the index
        if nums[i] >= target:
            return i
    # If target is greater than all elements, return the length of the array
    return len(nums)

# Example usage:
nums = [1, 3, 5, 6]
target = 5
result = search_insert(nums, target)
print(f"The target {target} should be inserted at index: {result}")


def search_insert(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


# Example usage:
nums = [1, 3, 5, 6]
target = 5
result = search_insert(nums, target)
print(f"The target {target} should be inserted at index: {result}")

