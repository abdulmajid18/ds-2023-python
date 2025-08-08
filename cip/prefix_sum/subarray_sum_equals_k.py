from typing import List

from typing import List


def subarraySumBrute(nums: List[int], k: int) -> int:
    count = 0
    n = len(nums)

    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += nums[end]
            if current_sum == k:
                count += 1

    return count



def subarraySum(nums: List[int], k: int) -> int:
    res = 0
    cur_sum = 0
    prefix_sums = {0 : 1}

    for n in nums:
        cur_sum += n
        diff = cur_sum - k

        res += prefix_sums.get(diff, 0)
        prefix_sums[cur_sum] = 1 + prefix_sums.get(cur_sum, 0)

    return res