from typing import List


class Solution:

    def longestConsecutiveBruteForce(self, nums: List[int]) -> int:
        """ O(n^2)"""
        if not nums:
            return 0

        max_len = 0

        for num in nums:
            current_num = num
            current_len = 1

            while current_num + 1 in nums:
                current_len += 1
                current_num += 1

            max_len = max(max_len, current_len)

        return max_len

    def longestConsecutiveBruteTwo(nums):
        """"""
        if not nums:
            return 0

        # Step 1: Sort the array
        nums.sort()

        # Step 2: Initialize the max length and current length of sequence
        max_len = 1
        current_len = 1

        # Step 3: Traverse the sorted array to find the longest consecutive sequence
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                # Skip duplicates
                continue
            elif nums[i] == nums[i - 1] + 1:
                # If current number is consecutive, increment the current sequence length
                current_len += 1
            else:
                # If not consecutive, reset the current sequence length
                max_len = max(max_len, current_len)
                current_len = 1

        # Compare the last sequence length with max length
        max_len = max(max_len, current_len)

        return max_len

    class Solution:
        def longestConsecutiveOptimized(self, nums: List[int]) -> int:
            if not nums:
                return 0

            max_len = 0
            num_set = set(nums)

            for num in nums:
                if (num - 1) not in num_set:
                    current_len = 0
                    while (num + current_len) in num_set:
                        current_len += 1
                    max_len = max(max_len, current_len)

            return max_len





