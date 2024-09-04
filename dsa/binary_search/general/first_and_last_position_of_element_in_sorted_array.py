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


def search_range(nums, target):
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        first_occurrence = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first_occurrence = mid
                right = mid - 1  # Keep searching on the left side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first_occurrence

    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        last_occurrence = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                last_occurrence = mid
                left = mid + 1  # Keep searching on the right side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last_occurrence

    first_occurrence = find_first(nums, target)
    last_occurrence = find_last(nums, target)

    return [first_occurrence, last_occurrence]


# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = search_range(nums, target)
print(f"The first and last position of {target} in the array are: {result}")
