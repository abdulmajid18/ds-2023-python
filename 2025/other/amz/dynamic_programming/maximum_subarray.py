from typing import List


class SolutionBruteOne:
    def maxSubArray(self, nums: List[int]) -> int:
        new_sum = float("-inf")
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                current_sum = sum(nums[i:j + 1])
                new_sum = max(new_sum, current_sum)
        return new_sum


class SolutionBruteTwo:
    def maxSubArray(self, nums: List[int]) -> int:
        new_sum = float("-inf")
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                new_sum = max(new_sum, current_sum)
        return new_sum



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub


class SolutionOptimized:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float("-inf")
        current_sum = 0

        for num in nums:
            current_sum = max(num, current_sum + num)  # Extend or start new subarray
            max_sum = max(max_sum, current_sum)  # Track max sum

        return max_sum
