from collections import defaultdict
from typing import List


def subarraysDivByKBruteForce(nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total % k == 0:
                count += 1
    return count


def subarraysDivByK(nums: List[int], k: int) -> int:
    prefix_sum = 0
    res = 0

    prefix_cnt = defaultdict(int)
    prefix_cnt[0] = 1

    for n in nums:
        prefix_sum += n
        remain = prefix_sum % k

        if remain in prefix_cnt:
            res += prefix_cnt[remain]

        prefix_cnt[remain] += 1

    return res











