from typing import List


def kthSmallestSubarraySum(nums: List[int], k: int) -> int:
    def check(threshold):
        count, left, total = 0, 0, 0
        for right, num in enumerate(nums):
            total += num
            while total > threshold:
                total -= nums[left]
                left += 1
            count += right - left + 1
        return count >= k

    left, right, res = min(nums), sum(nums), min(nums)
    while left <= right:
        mid = left + (right - left) // 2
        if check(mid):
            res = mid
            right = mid - 1
        else:
            left = mid + 1
    return res