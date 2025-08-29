from typing import List


def numSubarrayProductLessThanKBrute(nums: List[int], k: int) -> int:
    n = len(nums)
    count = 0
    for i in range(n):
        prod = 1
        for j in range(i, n):
            prod *= nums[j]
            if prod < k:
                count += 1
            else:
                break  # product will only grow, so break early
    return count


from typing import List


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    if k <= 1:
        return 0  # no valid subarray if k <= 1

    prod = 1
    left = 0
    count = 0

    for right in range(len(nums)):
        prod *= nums[right]

        while prod >= k:
            prod //= nums[left]
            left += 1

        count += right - left + 1

    return count

