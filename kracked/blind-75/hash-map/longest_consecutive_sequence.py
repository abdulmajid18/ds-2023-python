from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest


def longestConsecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Check if `num` is the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count sequence length
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak
