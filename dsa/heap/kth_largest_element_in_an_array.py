import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Initialize a min-heap of size k
        min_heap = []

        # Step 2: Build the heap by processing each element
        for num in nums:
            heapq.heappush(min_heap, num)

            # Ensure the heap size does not exceed k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Step 3: The root of the heap is the Kth largest element
        return min_heap[0]


def findKthLargest(self, nums: List[int], k: int) -> int:
    # Step 1: Convert nums into a max-heap by negating the elements
    max_heap = [-num for num in nums]  # Negate all elements to simulate a max-heap
    heapq.heapify(max_heap)  # Turn the list into a heap

    # Step 2: Pop from the heap k times
    kth_largest = -1
    for _ in range(k):
        kth_largest = -heapq.heappop(max_heap)  # Pop and negate to get the original value

    return kth_largest


from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def countGreaterEqual(t: int) -> int:
            return sum(num >= t for num in nums)

        low, high = min(nums), max(nums)
        while low < high:
            mid = (low + high) // 2
            if countGreaterEqual(mid) >= k:
                low = mid + 1
            else:
                high = mid
        return low - 1

import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quick_select(l, r) -> int:
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                quick_select(l, p - 1)
            elif p < k:
                quick_select(p + 1, r)
            else:
                return nums[p]

        return quick_select(0, len(nums) - 1)
