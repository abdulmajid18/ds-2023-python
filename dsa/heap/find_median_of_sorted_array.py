import heapq
from typing import List

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    left = []  # Max heap for the smaller half
    right = []  # Min heap for the larger half

    def add_number(num):
        # Push element into the correct heap and rebalance if necessary
        if len(left) == 0 or num < -left[0]:
            heapq.heappush(left, -num)  # Negate for max heap behavior
        else:
            heapq.heappush(right, num)

        # Rebalance the heaps if necessary
        if len(left) > len(right) + 1:
            heapq.heappush(right, -heapq.heappop(left))
        elif len(right) > len(left):
            heapq.heappush(left, -heapq.heappop(right))

    # Add numbers from both arrays
    for num in nums1:
        add_number(num)
    for num in nums2:
        add_number(num)

    # Calculate the median
    if len(left) > len(right):
        return -left[0]  # Max of left heap
    else:
        return (-left[0] + right[0]) / 2  # Average of max of left and min of right

# Example usage
nums1 = [1, 3]
nums2 = [2]
median = find_median_sorted_arrays(nums1, nums2)
print(median)  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
median = find_median_sorted_arrays(nums1, nums2)
print(median)  # Output: 2.5
