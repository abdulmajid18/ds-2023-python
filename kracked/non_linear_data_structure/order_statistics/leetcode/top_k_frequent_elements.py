from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    from collections import Counter
    freq = Counter(nums)

    max_heap = [(-v, k) for (k, v) in freq.items()]
    import heapq
    heapq.heapify(max_heap)

    res = []
    for _ in range(k):
        res.append(heapq.heappop(max_heap)[1])

    return res

from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequentTwo(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        max_heap = [(-cnt, num) for num, cnt in freq.items()]
        heapq.heapify(max_heap)
        return [heapq.heappop(max_heap)[1] for _ in range(k)]


from collections import Counter
from typing import List


class Solution:
    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        # Buckets: index = frequency, value = list of numbers
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        res = []
        # Traverse buckets from high freq to low
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res
        return None
