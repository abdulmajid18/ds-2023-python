from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(nums, candidate, used, res):
            if len(candidate) == len(nums):
                res.append(candidate[:])
                return
            for num in nums:
                if num not in used:
                    candidate.append(num)
                    used.add(num)
                    backtrack(nums, candidate, used, res)
                    candidate.pop()
                    used.remove(num)

        backtrack(nums, [], set(), res)
        return res
