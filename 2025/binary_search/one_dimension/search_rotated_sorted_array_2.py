from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return True

            # Handle duplicates by shrinking the search space
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue

            # Check if left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:  # Target is in the left half
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[r]:  # Target is in the right half
                    l = mid + 1
                else:
                    r = mid - 1

        return False  # Target not found
