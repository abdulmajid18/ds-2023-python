from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_set = set(nums)

        for n in range(len(nums) + 1):
            if n not in num_set:
                return n

    def missingNumberXOROptimized(self, nums: List[int]) -> int:
        missing_num = 0

        for i in range(len(nums) + 1):
            missing_num ^= i

        for num in nums:
            missing_num ^= num

        return missing_num


