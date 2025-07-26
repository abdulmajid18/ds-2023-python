from typing import List


class Solution:
    def searchRangeBruteForce(self, nums: List[int], target: int) -> List[int]:
        start, end = -1, -1

        for i, n in enumerate(nums):
            if n == target:
                if start == -1:
                    start = i
                end = i

        return [start, end]

from typing import List

def searchRange(self, nums: List[int], target: int) -> List[int]:
    def find_first():
        l, r = 0, len(nums) - 1
        index = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                index = m
                r = m - 1
        return index

    def find_last():
        l, r = 0, len(nums) - 1
        index = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                index = m
                l = m + 1
        return index

    return [find_first(), find_last()]

