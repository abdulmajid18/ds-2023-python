import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        heap = [(-v, k) for k, v in counter.items()]
        heapq.heapify(heap)
        result = []

        for _ in range(k):
            largest = heapq.heappop(heap)
            result.append(largest[1])

        return result
