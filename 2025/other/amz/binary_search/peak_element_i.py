from typing import List


def findPeakElementBruteForce(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        left = nums[i - 1] if i > 0 else float("-inf")
        mid = nums[i]
        right = nums[i + 1] if i < n - 1 else float('-inf')
        if mid > left and mid > right:
            return i
    return -1


class Solution:
    pass


def findPeakElement(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l)) // 2

        if m > 0 and nums[m] < nums[m - 1]:
            r = m - 1
        elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
            l = m + 1
        else:
            return m
