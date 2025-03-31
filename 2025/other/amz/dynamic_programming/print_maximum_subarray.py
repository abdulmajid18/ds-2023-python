from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> List[int]:
        max_sum = float("-inf")
        current_sum = 0
        start = end = 0  # Start and end indices of the max subarray
        temp_start = 0  # Temporary start index for a new subarray

        for i in range(len(nums)):
            if current_sum + nums[i] > nums[i]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]
                temp_start = i  # Start new subarray from this index

            if current_sum > max_sum:
                max_sum = current_sum
                start = temp_start  # Update start index of max subarray
                end = i  # Update end index of max subarray

        print(f"Maximum sum: {max_sum}")
        print(f"Subarray: {nums[start:end + 1]}")  # Extract subarray

        return nums[start:end + 1]


# Example Usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
sol = Solution()
sol.maxSubArray(nums)
