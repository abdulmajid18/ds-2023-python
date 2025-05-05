from collections import Counter
import heapq

from typing import List
from collections import Counter


def topKFrequentOne(nums: List[int], k: int) -> List[int]:
    from collections import Counter
    freq_map = Counter(nums)

    import heapq
    freq_list = [(-freq, num) for num, freq in freq_map.items()]
    heapq.heapify(freq_list)

    top_k = [heapq.heappop(freq_list)[1] for _ in range(k)]
    return top_k



def topKFrequentTwo(nums, k):
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


def topKFrequentBucketSort(nums: List[int], k: int) -> List[int]:

    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    bucket = [[] for _ in range(len(nums) + 1)]

    for num, freq in counter.items():
        bucket[freq].append(num)

    res = []
    for i in range(len(bucket) - 1, -1, -1):
        for n in bucket[i]:
            res.append(n)
        if len(res) == k:
            return res