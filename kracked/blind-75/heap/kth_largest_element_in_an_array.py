import heapq
def kth_largest_good(nums, k):

    # heapify the elemnte ... we need to pop the largest so we  use a max heap
    nums = [-num for num in nums]
    heapq.heapify(nums)

    res = 0

    for _ in range(k):
        res = -1 * heapq.heappop(nums)

    return res


import heapq


def kth_largest_better(nums, k):
    # Create a min-heap of size k
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    # The root of the heap is the k-th largest element
    return min_heap[0]


from typing import List


def findKthLargest(nums: List[int], k: int) -> int:
    kth = len(nums) - k

    def quickSelect(l, r):
        pivot = nums[r]
        p = l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > kth:
            return quickSelect(l, p - 1)
        elif p < kth:
            return quickSelect(p + 1, r)
        else:
            return nums[p]

    return quickSelect(0, len(nums) - 1)