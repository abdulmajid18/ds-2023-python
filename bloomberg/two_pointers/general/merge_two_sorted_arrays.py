from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Start from the end of nums1 array
        p1 = m - 1  # Pointer for the last element in the initialized part of nums1
        p2 = n - 1  # Pointer for the last element in nums2
        p = m + n - 1  # Pointer for the last element in nums1

        # Merge nums1 and nums2 from the back to the front
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are remaining elements in nums2, copy them to nums1
        # No need to check nums1, because it's already in place
        nums1[:p2 + 1] = nums2[:p2 + 1]
