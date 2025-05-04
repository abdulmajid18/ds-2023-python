from typing import List


def subarrays_with_k_distinct_brute_1(nums, k):
    n = len(nums)
    count = 0
    for i in range(n):
        for j in range(i, n):
            subarray = nums[i:j + 1]
            distinct_count = len(set(subarray))
            if distinct_count == k:
                count += 1
    return count


def count_subarrays_with_k_distinct_brute_set(nums: list[int], k: int) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        distinct = set()
        for j in range(i, n):
            distinct.add(nums[j])
            if len(distinct) == k:
                count += 1
            elif len(distinct) > k:
                break
    return count


def subarraysWithKDistinctBruteThree(nums: List[int], k: int) -> int:
    n = len(nums)
    res = 0

    for i in range(n):
        from collections import defaultdict
        freq = defaultdict(int)
        distinct = 0
        for j in range(i, n):
            if freq[nums[j]] == 0:
                distinct += 1
            freq[nums[j]] += 1

            if distinct == k:
                res += 1
            elif distinct > k:
                break
    return res


from collections import defaultdict

from collections import defaultdict


def subarraysWithKDistinct(nums: list[int], k: int) -> int:
    return _at_most_k(nums, k) - _at_most_k(nums, k - 1)


def _at_most_k(nums: list[int], k: int) -> int:
    """Return count of subarrays with ≤ k distinct numbers."""
    if k < 0:  # guard for k‑1 when k==0
        return 0

    freq = defaultdict(int)  # element → frequency in window
    left = 0
    res = 0  # answer to build

    for right, x in enumerate(nums):
        if freq[x] == 0:  # new distinct element enters window
            k -= 1
        freq[x] += 1

        # shrink until window has ≤ k distinct
        while k < 0:
            y = nums[left]
            freq[y] -= 1
            if freq[y] == 0:
                k += 1  # one distinct element removed
            left += 1

        res += right - left + 1  # all subarrays ending at right
    return res
