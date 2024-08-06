def threeSumClosestBruteForce(nums, target):
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                current_sum = nums[i] + nums[j] + nums[k]
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

    return closest_sum

# Example usage
nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosestBruteForce(nums, target))  # Output: 2

nums = [1, 1, 1, 1]
target = 2
print(threeSumClosestBruteForce(nums, target))  # Output: 3


def threeSumClosestOptimized(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                return current_sum

    return closest_sum

# Example usage
nums = [-1, 2, 1, -4]
target = 1
print(threeSumClosestOptimized(nums, target))  # Output: 2

nums = [1, 1, 1, 1]
target = 2
print(threeSumClosestOptimized(nums, target))  # Output: 3
