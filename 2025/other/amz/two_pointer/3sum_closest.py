from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float("inf")

        for i, v in enumerate(nums):
            l, r = i + 1, len(nums) - 1

            while l < r:
                current_sum = v + nums[l] + nums[r]
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

                if current_sum < target:
                    l += 1
                elif current_sum > target:
                    r -= 1
                else:
                    return current_sum
        return closest_sum


def three_sum_closest_brute_force(nums, target):
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                current_sum = nums[i] + nums[j] + nums[k]

                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum

    return closest_sum

