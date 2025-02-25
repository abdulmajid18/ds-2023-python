from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Given a binary array nums and an integer k, the goal is to find the longest contiguous subarray
        that contains at most k zeroes.

        The approach uses a sliding window with two pointers:
        - Expand the window by moving the right pointer (r) and count the number of zeroes.
        - If the number of zeroes exceeds k, shrink the window from the left (l) until it becomes valid again.
        - Keep track of the maximum valid window size encountered during the process.

        This ensures an optimal O(N) solution, as each element is processed at most twice (once when expanding
        and once when contracting the window).
        """
        res = 0
        l = 0
        zero_count = 0

        for r, v in enumerate(nums):
            if v == 0:
                zero_count += 1

            while zero_count > k:
                if nums[l] == 0:
                    zero_count -= 1
                l += 1

            res = max(res, r - l + 1)
        return res


class Solution:
    def longestOnesBruteForce(self, nums: List[int], k: int) -> int:
        """
        Brute force approach:
        - Iterate through all subarrays and count the number of zeros.
        - If the number of zeros is within k, update the maximum length.
        - Time Complexity: O(N^2)
        """
        n = len(nums)
        max_length = 0

        for i in range(n):
            zero_count = 0
            for j in range(i, n):
                if nums[j] == 0:
                    zero_count += 1
                if zero_count > k:
                    break
                max_length = max(max_length, j - i + 1)

        return max_length
