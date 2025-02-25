from typing import List


class Solution:
    def findMaxConsecutiveOnesBruteForce(self, nums: List[int]) -> int:
        res = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    break
                res = max(res, j - i + 1)
        return res


class Solution:
    def findMaxConsecutiveOnesOptimized(self, nums: List[int]) -> int:
        res = 0
        l = 0
        for i, v in enumerate(nums):
            if v == 0:
                l = i + 1
            res = max(res, i - l + 1)
        return res
