from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Sort the array
        nums.sort()

        longest = 1
        current_length = 1

        # Iterate through the array to find the longest consecutive sequence
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:  # Skip duplicates
                continue
            if nums[i] == nums[i - 1] + 1:  # Consecutive elements
                current_length += 1
            else:  # Reset the length
                longest = max(longest, current_length)
                current_length = 1  # Start new sequence

        # Return the longest consecutive sequence found
        return max(longest, current_length)


# Example usage:
sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Output: 4
print(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Output: 9
print(sol.longestConsecutive([1, 0, 1, 2]))  # Output: 3


class SolutionOptimized:
    def longestConsecutive(self, nums: List[int]) -> int:
            numSet = set(nums)
            longest = 0

            for n in nums:
                if (n - 1) not in numSet:
                    length = 0
                    while (n + length) in numSet:
                        length += 1
                longest = max(length, longest)
            return longest