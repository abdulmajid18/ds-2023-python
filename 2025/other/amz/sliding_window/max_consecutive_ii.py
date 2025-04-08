"""Input: [1,0,1,1,0]
Try flipping index 1 → [1,1,1,1,0] → streak = 4
Try flipping index 4 → [1,0,1,1,1] → streak = 4
Return 4"""
from typing import List

"""🔧 Problem: Max Consecutive Ones II
Given a binary array nums, you can flip at most one 0 to 1.
Return the maximum number of consecutive 1s in the array if you can flip at most one 0."""


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_len = 0

    for i in range(len(nums)):
        # Try flipping nums[i] if it's 0
        if nums[i] == 0:
            nums[i] = 1  # Flip 0 to 1

            # Count longest streak of 1s
            count = 0
            temp_max = 0
            for num in nums:
                if num == 1:
                    count += 1
                    temp_max = max(temp_max, count)
                else:
                    count = 0

            max_len = max(max_len, temp_max)
            nums[i] = 0  # Restore original value

    # Also check case where no 0s are flipped (i.e., array has no 0s)
    count = 0
    temp_max = 0
    for num in nums:
        if num == 1:
            count += 1
            temp_max = max(temp_max, count)
        else:
            count = 0
    max_len = max(max_len, temp_max)

    return max_len


nums = [1, 0, 1, 1, 0]
a = findMaxConsecutiveOnes(nums)
print(a)


def findMaxConsecutiveOnes(nums: List[int]) -> int:
    left = 0
    max_len = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len


nums = [1, 0, 1, 1, 0]
a = findMaxConsecutiveOnes(nums)
print(a)
