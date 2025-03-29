def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i


def twoSum(nums, target):
    nums_with_index = [(num, i) for i, num in enumerate(nums)]
    nums_with_index.sort()

    left, right = 0, len(nums) - 1

    while left < right:
        current_sum = nums_with_index[left][0] + nums_with_index[right][0]

        if current_sum == target:
            return [nums_with_index[left][1], nums_with_index[right][1]]
        elif current_sum < target:
            left += 1  # Move left pointer to increase sum
        else:
            right -= 1  # Move right pointer to decrease sum
