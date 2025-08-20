from typing import List


def countSmallerBruteForce(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    for i in range(n):
        cur_num = nums[i]
        count = 0
        for j in range(i + 1, n):
            if cur_num > nums[j]:
                count += 1
        res[i] = count
    return res


class Solution:
    pass

