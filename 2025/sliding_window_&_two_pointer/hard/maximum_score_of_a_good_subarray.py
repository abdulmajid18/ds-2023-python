from typing import List


class Solution:
    def maximumScoreBruteForce(self, nums: List[int], k: int) -> int:
        max_score = 0
        n = len(nums)
        for i in range(k, -1, -1):
            for j in range(k, n):
                min_val = min(nums[i:j + 1])
                score = min_val * (j - i + 1)
                max_score = max(max_score, score)
        return max_score



class Solution2:
    def maximumScore(self, nums: List[int], k: int) -> int:
        # Initialize pointers and variables
        l, r = k, k  # Start with the subarray [k, k]
        res = nums[k]  # Initial score is nums[k] * 1
        cur_min = nums[k]  # Current minimum in the subarray

        # Expand the subarray to the left or right
        while l >= 0 and r < len(nums):
            # Get the next left and right elements
            left = nums[l - 1] if l > 0 else float('-inf')  # Out of bounds: -inf
            right = nums[r + 1] if r < len(nums) - 1 else float('-inf')  # Out of bounds: -inf

            # Expand in the direction of the larger element
            if left > right:
                l -= 1  # Expand left
                cur_min = min(cur_min, left)  # Update the minimum
            else:
                r += 1  # Expand right
                cur_min = min(cur_min, right)  # Update the minimum

            # Calculate the score of the current subarray
            res = max(res, cur_min * (r - l + 1))

        return res