from typing import List


def findMedianSortedArraysBruteOne(nums1: List[int], nums2: List[int]) -> float:
    merged = sorted(nums1 + nums2)
    total = len(merged)

    if total % 2 == 1:
        return float(merged[total // 2])
    else:
        mid1 = merged[total // 2 - 1]
        mid2 = merged[total // 2]
        return (mid1 + mid2) / 2


def findMedianSortedArrays(nums1, nums2):
    def merge_sorted_arrays(nums1, nums2):
        i, j = 0, 0
        merged = []

        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        while i < len(nums1):
            merged.append(nums1[i])
            i += 1

        while j < len(nums2):
            merged.append(nums2[j])
            j += 1

        return merged

    merged = merge_sorted_arrays(nums1, nums2)
    total = len(merged)

    if total % 2 == 1:
        return float(merged[total // 2])
    else:
        mid = total // 2
        return (merged[mid - 1] + merged[mid]) / 2.0


a = [1,2,3,4,5]
print(13//2)