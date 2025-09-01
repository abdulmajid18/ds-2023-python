from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []

        l, r = 0, 0
        l_len, r_len = len(nums1), len(nums2)

        while l < l_len and r < r_len:
            if nums1[l] < nums2[r]:
                merged.append(nums1[l])
                l += 1
            else:
                merged.append(nums2[r])
                r += 1

        if l < l_len:
            merged.extend(nums1[l:])
        if r < r_len:
            merged.extend(nums2[r:])

        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            return (merged[n // 2 - 1] + merged[n // 2]) / 2.0
