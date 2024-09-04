def sortColorsBruteForce(nums):
    # Count the occurrences of 0s, 1s, and 2s
    count = [0, 0, 0]
    for num in nums:
        count[num] += 1

    # Reconstruct the sorted array based on counts
    index = 0
    for color in range(3):
        for _ in range(count[color]):
            nums[index] = color
            index += 1


def sortColors(nums):
    left, mid, right = 0, 0, len(nums) - 1

    while mid <= right:
        if nums[mid] == 0:
            nums[left], nums[mid] = nums[mid], nums[left]
            left += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1


# Example usage
nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]
