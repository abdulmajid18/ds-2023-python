
from collections import Counter
from typing import List

class SolutionBruteForce:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        for v, f in freq.items():  # Fixed iteration
            if f > len(nums) // 2:
                return v  # Fixed return statement


from collections import Counter
from typing import List


class SolutionImprovement:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        maxCount = 0
        res = 0
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
            res = n if freq[n] > maxCount else res
            maxCount = max(maxCount, freq[n])

        return res


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n

            count += (1 if n == res else -1)
        return res

