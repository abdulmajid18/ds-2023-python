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
        left, right = k, k  # We start the interval at the element nums[k]
        min_val = nums[k]  # The minimum value in the initial interval
        max_score = nums[k]  # The score of the initial subarray (nums[k])

        # Expand the subarray by moving both left and right
        while left >= 0 or right < len(nums):
            # We need to expand on either the left or right side
            if left >= 0 and (right >= len(nums) or nums[left] >= nums[right]):
                min_val = min(min_val, nums[left])
                left -= 1  # Expand left
            else:
                min_val = min(min_val, nums[right])
                right += 1  # Expand right

            # Calculate the score of the current subarray
            score = min_val * (right - left - 1)
            max_score = max(max_score, score)  # Update max score if needed

        return max_score


class Solution3:
    def maximumScore(self, nums: List[int], k: int) -> int:
        l, r = k, k  # Start with the initial position at k
        res = nums[k]  # Initially, the score is nums[k] * 1
        cur_min = nums[k]  # The minimum value in the current subarray

        # Expand the window as long as the pointers are valid
        while l >= 0 and r < len(nums):
            # Calculate the possible next left and right values
            left = nums[l - 1] if l > 0 else float('inf')  # Set left to infinity if out of bounds
            right = nums[r + 1] if r < len(nums) - 1 else float('inf')  # Set right to infinity if out of bounds

            # Expand the window in the direction of the larger element to maintain a high min value
            if left <= right:
                l -= 1
                cur_min = min(cur_min, nums[l])
            else:
                r += 1
                cur_min = min(cur_min, nums[r])

            # Calculate the score for the current subarray
            res = max(res, cur_min * (r - l + 1))

        return res
