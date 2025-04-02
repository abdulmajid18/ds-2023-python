from typing import List


class Solution:
    def maxLen(self, nums: List[int]) -> int:
        # Dictionary to store the first occurrence of a prefix sum
        prefix_sum_map = {}
        prefix_sum = 0
        max_length = 0

        for i in range(len(nums)):
            # Update the prefix sum
            prefix_sum += nums[i]

            # If the prefix sum is zero, the subarray from index 0 to i has a sum of zero
            if prefix_sum == 0:
                max_length = i + 1

            # If the prefix sum is already in the dictionary, update the max_length
            elif prefix_sum in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[prefix_sum])

            # Store the first occurrence of the prefix sum
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i

        return max_length
