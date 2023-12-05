from typing import List


def findMedianSortedArrays(nums1, nums2):
    nums = sorted(nums1 + nums2)
    n = len(nums)

    if n % 2 == 0:
        # If the total number of elements is even, return the average of the middle two elements
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    else:
        # If the total number of elements is odd, return the middle element
        return nums[n // 2]


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]):
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2

    if len(A) > len(B):
        A, B = B, A

    l, r = 0, len(A) - 1
    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i >= 0 else float('-infinity')
        Aright = A[i + 1] if (i + 1) < len(A) else float('infinity')
        Bleft = B[j] if j >= 0 else float('-infinity')
        Bright = B[j + 1] if (j + 1) < len(A) else float('infinity')

        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright, Bright)
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1
