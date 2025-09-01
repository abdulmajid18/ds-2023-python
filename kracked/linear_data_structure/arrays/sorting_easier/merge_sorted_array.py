from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    merged = []
    i, j = 0, 0

    while i < m and j < n:
        # check if m to be moved
        if nums1[i] < nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    while i < m:
        merged.append(nums1[i])
        i += 1

    while j < n:
        merged.append(nums2[j])
        j += 1

    for i in range(m + n):
        nums1[i] = merged[i]

def mergeTwo(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
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