from typing import List


def findDisappearedNumbersBrute(nums: List[int]) -> List[int]:
    num_set = set(nums)
    n = len(nums)
    res = []
    for i in range(1, n+1):
        if i not in num_set:
            res.append(i)
    return res


def findDisappearedNumbersOptimized(nums: List[int]) -> List[int]:
    for x in nums:
        idx = abs(x) - 1
        if nums[idx] > 0:
            nums[idx] *= -1   # mark visited

    res = []
    for i, x in enumerate(nums):
        if x > 0:   # not visited
            res.append(i + 1)
    return res

