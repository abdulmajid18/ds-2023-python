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
        def partition(left: int, right: int, pivot_index: int) -> int:
            pivot_value = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            store_index = left
            for i in range(left, right):
                if nums[i] > pivot_value:
                    nums[store_index], nums[i] = nums[i], nums[store_index]
                    store_index += 1
            nums[right], nums[store_index] = nums[store_index], nums[right]
            return store_index

        def quick_select(left: int, right: int, k_smallest: int) -> int:
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return quick_select(left, pivot_index - 1, k_smallest)
            else:
                return quick_select(pivot_index + 1, right, k_smallest)

        return quick_select(0, len(nums) - 1, k - 1)
