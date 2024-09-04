from typing import List


def findMedianSortedArraysBrute(nums1, nums2):
    # Merge the two sorted arrays
    merged_array = sorted(nums1 + nums2)

    # Find the median
    n = len(merged_array)
    if n % 2 == 1:
        # Odd length: return the middle element
        return merged_array[n // 2]
    else:
        # Even length: return the average of the two middle elements
        mid1 = n // 2
        mid2 = mid1 - 1
        return (merged_array[mid1] + merged_array[mid2]) / 2


# Example usage:
print(5//2)
print(5/2)
nums1 = [1, 3]
nums2 = [2]
result = findMedianSortedArraysBrute(nums1, nums2)
print("Median of the two sorted arrays is:", result)

nums1 = [1, 2]
nums2 = [3, 4]
result = findMedianSortedArraysBrute(nums1, nums2)
print("Median of the two sorted arrays is:", result)

import heapq


def findMedianSortedArraysHeap(self, nums1: List[int], nums2: List[int]) -> float:
    min_heap = []

    for num in nums1:
        heapq.heappush(min_heap, num)

    for num in nums2:
        heapq.heappush(min_heap, num)

    merged_array = [heapq.heappop(min_heap) for _ in range(len(min_heap))]

    n = len(merged_array)
    if n % 2 == 1:
        # Odd length: return the middle element
        return merged_array[n // 2]
    else:
        # Even length: return the average of the two middle elements
        mid1 = n // 2
        mid2 = mid1 - 1
        return (merged_array[mid1] + merged_array[mid2]) / 2


def findMedianSortedArraysOptimized(self, nums1: List[int], nums2: List[int]) -> float:
    left = []
    right = []

    # Push element into the correct heap and rebalance if necessary
    def add_number(num):
        # python has no max heap, so we negate the left to mimic it, so it will pop that largest value ie the largest
        # negative val
        if len(left) == 0 or num < -left[0]:
            heapq.heappush(left, -num)
        else:
            heapq.heappush(right, num)

        # Rebalance the heaps if necessary
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))

    for num in nums1:
        add_number(num)
    for num in nums2:
        add_number(num)

    if len(left) > len(right):
        return -left[0]
    else:
        return (-left[0] + right[0]) / 2
