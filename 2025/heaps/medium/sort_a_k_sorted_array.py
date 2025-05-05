import heapq
from typing import List


def sortKSortedArray(arr: List[int], k: int) -> List[int]:
    heap = []
    result = []

    for i in range(min(k + 1, len(arr))):
        heapq.heappush(heap, arr[i])

    for i in range(k + 1, len(arr)):
        result.append(heapq.heappop(heap))
        heapq.heappush(heap, arr[i])

    while heap:
        result.append(heapq.heappop(heap))

    return result


arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
print(sortKSortedArray(arr, k))

import heapq


def sort_k_sorted(nums, k):
    """
    Sort an array where each element is no more than k positions
    away from its target position.
    Time  : O(n log k)
    Space : O(k)
    """
    n = len(nums)
    if n <= 1 or k <= 0:
        return nums[:]

    heap = nums[:k + 1]
    heapq.heapify(heap)

    out = []
    for i in range(k + 1, n):
        out.append(heapq.heappop(heap))  # smallest of window
        heapq.heappush(heap, nums[i])  # add next element

    while heap:
        out.append(heapq.heappop(heap))

    return out


def sort_k_sorted_inplace(a, k):
    heap = a[:k + 1]
    heapq.heapify(heap)
    target = 0

    for i in range(k + 1, len(a)):
        a[target] = heapq.heappop(heap)
        heapq.heappush(heap, a[i])
        target += 1

    while heap:
        a[target] = heapq.heappop(heap)
        target += 1
