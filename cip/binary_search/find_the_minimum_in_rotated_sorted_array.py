from typing import List


def findMin(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[r]:
            l = mid + 1
        else:
            r = mid
    return nums[l]


def findMinTwo(nums):
    i, j = 0, len(nums) - 1
    while i < j:
        mid = (i + j) // 2
        if nums[mid] >= nums[0]:
            i = mid + 1
        else:
            j = mid
    return nums[i]
