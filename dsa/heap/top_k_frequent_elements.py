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


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

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