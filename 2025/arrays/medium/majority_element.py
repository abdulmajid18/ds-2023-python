from collections import Counter
from typing import List


class Solution:
    def majorityElementHashMap(self, nums: List[int]) -> int:
        freq_map = Counter(nums)

        for k, v in freq_map.items():
            if v > len(nums) // 2:
                return k

    def majorityElementBruteForce(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1
            if count > n // 2:
                return nums[i]

    def majorityElementHashMapTwo(self, nums: List[int]) -> int:
        freq_map = {}  # Dictionary to store frequency counts
        n = len(nums)

        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1  # Increment count

            if freq_map[num] > n // 2:  # Check majority condition
                return num