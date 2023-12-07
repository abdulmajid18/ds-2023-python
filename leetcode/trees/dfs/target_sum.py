def findWaysToEvaluate(nums, target):
    def dfs(index, current_sum):
        if index == len(nums):
            if current_sum == target:
                return 1
            else:
                return 0

        # Calculate the number of ways with a '+' sign
        ways_plus = dfs(index + 1, current_sum + nums[index])

        # Calculate the number of ways with a '-' sign
        ways_minus = dfs(index + 1, current_sum - nums[index])

        return ways_plus + ways_minus

    return dfs(0, 0)

# Example usage:
nums = [2, 1]
target = 1
result = findWaysToEvaluate(nums, target)
print(result)
