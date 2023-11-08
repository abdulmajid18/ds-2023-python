import heapq
from typing import List


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    element_count = {}
    for num in nums:
        element_count[num] = element_count.get(num, 0) + 1

    # Create a max heap to store elements based on their frequency
    max_heap = [(-count, num) for num, count in element_count.items()]
    heapq.heapify(max_heap)

    top_k = []
    for _ in range(k):
        count, num = heapq.heappop(max_heap)
        top_k.append(num)

    return top_k
