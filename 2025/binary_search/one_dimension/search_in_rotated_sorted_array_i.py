from typing import List


def searchBruteForce(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            # Determine the sorted portion
            if nums[left] <= nums[mid]:  # Left portion is sorted
                if nums[left] <= target < nums[mid]:  # Target is in the left portion
                    right = mid - 1
                else:  # Target is in the right portion
                    left = mid + 1
            else:  # Right portion is sorted
                if nums[mid] < target <= nums[right]:  # Target is in the right portion
                    left = mid + 1
                else:  # Target is in the left portion
                    right = mid - 1

        return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
result = Solution().search(nums, target)
print(result)  # Expected output: -1 (target 3 is not in the array)

