from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    n = len(nums)

    # Step 1: Clean the array
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    # Step 2: Mark presence
    for num in nums:
        if 1 <= abs(num) <= n:
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

    # Step 3: Find missing positive
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    return n + 1