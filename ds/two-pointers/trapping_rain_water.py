from typing import List


def trapBruteForce(height):
    n = len(height)
    trapped_water = 0

    for i in range(1, n - 1):
        left_max = max(height[:i])
        right_max = max(height[i + 1:])
        current_water = max(0, min(left_max, right_max) - height[i])
        trapped_water += current_water

    return trapped_water


def trap(self, height: List[int]) -> int:
    nums = height
    maxRight = [0] * len(nums)
    maxLeft = [0] * len(nums)
    minLeftRight = [0] * len(nums)

    leftMax = 0
    for i in range(1, len(nums)):
        leftMax = max(leftMax, nums[i - 1])
        maxLeft[i] = leftMax

    rightMax = 0
    for j in range(len(nums) - 2, -1, -1):
        rightMax = max(rightMax, nums[j + 1])
        maxRight[j] = rightMax

    for k in range(len(nums)):
        minLeftRight[k] = min(maxRight[k], maxLeft[k])

    trappedWater = 0
    for i in range(len(nums)):
        trapped = minLeftRight[i] - nums[i]
        if trapped >= 0:
            trappedWater += trapped
    return trappedWater


def trapOptimized(height):
    n = len(height)
    if n <= 2:
        return 0

    left, right = 0, n - 1
    left_max, right_max = 0, 0
    trapped_water = 0

    while left < right:
        left_max = max(left_max, height[left])
        right_max = max(right_max, height[right])

        if height[left] < height[right]:
            trapped_water += max(0, left_max - height[left])
            left += 1
        else:
            trapped_water += max(0, right_max - height[right])
            right -= 1

    return trapped_water
