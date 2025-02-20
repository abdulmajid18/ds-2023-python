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
