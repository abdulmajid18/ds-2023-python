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


def search_range(nums, target):
    def find_first(nums, target):
        left, right = 0, len(nums) - 1
        first_occurrence = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first_occurrence = mid
                right = mid - 1  # Keep searching on the left side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first_occurrence

    def find_last(nums, target):
        left, right = 0, len(nums) - 1
        last_occurrence = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                last_occurrence = mid
                left = mid + 1  # Keep searching on the right side
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last_occurrence

    first_occurrence = find_first(nums, target)
    last_occurrence = find_last(nums, target)

    return [first_occurrence, last_occurrence]


# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
result = search_range(nums, target)
print(f"The first and last position of {target} in the array are: {result}")


