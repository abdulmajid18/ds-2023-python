from collections import Counter
import heapq


def topKFrequent(nums, k):
    # Step 1: Count frequencies
    freq_map = Counter(nums)  # {num: frequency}

    # Step 2: Use a min-heap to keep the top k elements
    min_heap = []
    for num, freq in freq_map.items():
        heapq.heappush(min_heap, (freq, num))  # Push frequency and number
        if len(min_heap) > k:  # Ensure heap size is k
            heapq.heappop(min_heap)

    # Step 3: Extract the elements from the heap
    return [num for freq, num in min_heap]
