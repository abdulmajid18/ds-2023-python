from typing import List


class Solution:
    """
    This solution finds the first and last occurrence of a target value in a sorted array using binary search.

    **Approach:**
    - Since the array is sorted, we can leverage **binary search** instead of a linear scan (O(n)), achieving O(log n) complexity.
    - We implement two separate binary search functions:
      1. `find_first(nums, target)`: Finds the **first occurrence** of `target`.
      2. `find_last(nums, target)`: Finds the **last occurrence** of `target`.

    **Binary Search Explanation:**
    - **Finding the first occurrence:**
      - Perform binary search and **store the index when `nums[mid] == target`**.
      - Move `r = mid - 1` to search in the left half for an earlier occurrence.
      - The last stored index is the first occurrence.

    - **Finding the last occurrence:**
      - Perform binary search and **store the index when `nums[mid] == target`**.
      - Move `l = mid + 1` to search in the right half for a later occurrence.
      - The last stored index is the last occurrence.

    **Time Complexity:** O(log n) for both searches → **Total: O(log n)**.
    **Space Complexity:** O(1), as no extra space is used.
    """

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target):
            l, r = 0, len(nums) - 1
            first = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    first = mid  # Store the position
                    r = mid - 1  # Search left for an earlier occurrence
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return first

        def find_last(nums, target):
            l, r = 0, len(nums) - 1
            last = -1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    last = mid  # Store the position
                    l = mid + 1  # Search right for a later occurrence
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return last

        first = find_first(nums, target)
        last = find_last(nums, target)

        return [first, last]


# Example test cases
sol = Solution()
print(sol.searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3,4]
print(sol.searchRange([5, 7, 7, 8, 8, 10], 6))  # Output: [-1,-1]
print(sol.searchRange([], 0))  # Output: [-1,-1]
print(sol.searchRange([2, 2, 2, 2, 2], 2))  # Output: [0,4]
print(sol.searchRange([1, 2, 3, 4, 5], 3))  # Output: [2,2]
