from typing import List


def threeSumClosestA(self, nums: List[int], target: int) -> int:
    nums.sort()
    resultSum = nums[0] + nums[1] + nums[2]
    minDif = float("inf")

    for i in range(len(nums)):
        l, r = i + 1, len(nums) - 1

        while l < r:
            threeSum = nums[i] + nums[l] + nums[r]
            if threeSum == target:
                return target
            elif threeSum < target:
                l += 1
            else:
                r -= 1

            diffToTarget = abs(threeSum - target)
            if diffToTarget < minDif:
                resultSum = threeSum
                minDif = diffToTarget
    return resultSum


def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum > target:
                right -= 1
            else:
                left += 1

    return closest_sum
