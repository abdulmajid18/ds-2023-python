from typing import List


def longestEqualSubarrayBruteForce(nums: List[int], k: int) -> int:
    max_len = 0
    n = len(nums)

    for start in range(n):
        freq = {}
        max_freq = 0
        for end in range(start, n):
            num = nums[end]
            freq[num] = freq.get(num, 0) + 1
            max_freq = max(max_freq, freq[num])

            length = end - start + 1
            deletions = length - max_freq

            if deletions <= k:
                max_len = max(max_len, max_freq)
    return max_len

