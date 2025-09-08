from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for k, v in enumerate(nums):
            expected_num = target - v
            if expected_num in hash_map:
                return hash_map[expected_num], k
            else:
                hash_map[v] = k

