from typing import List


def numberOfSubarrays(nums: List[int], k: int) -> int:
    count = 0
    n = len(nums)

    for start in range(n):
        odd_count = 0
        for end in range(start, n):
            if nums[end] % 2 == 1:
                odd_count += 1
            if odd_count == k:
                count += 1
            elif odd_count > k:
                break  # No need to keep going
    return count
