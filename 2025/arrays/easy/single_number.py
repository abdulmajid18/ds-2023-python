from collections import defaultdict
from typing import List


class Solution:
    def singleNumberBruteForce(self, nums: List[int]) -> int:
        from collections import Counter
        freq_map = Counter(nums)

        for i, k in freq_map.items():
            if k == 1:
                return i

    def singleNumbeBruteTwo(self, nums):
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        for num in count:
            if count[num] == 1:
                return num

    def singleNumberSet(self, nums):
        unique_numbers = set()

        for num in nums:
            if num in unique_numbers:
                unique_numbers.remove(num)
            else:
                unique_numbers.add(num)

        return unique_numbers.pop()

    def singleNumberOptimized(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res = n ^ res
        return res
