from typing import List


def kSmallestPairsBruteForceOne(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    arr = []
    for u in nums1:
        for v in nums2:
            arr.append([u, v])

    arr.sort(key=lambda x: x[0] + x[1])
    return arr[:k]


def kSmallestPairsBruteForceTwo(nums1, nums2, k):
    all_pairs = []

    for i in range(len(nums1)):
        for j in range(len(nums2)):
            total = nums1[i] + nums2[j]
            all_pairs.append((total, nums1[i], nums2[j]))

    all_pairs.sort()

    result = [[u, v] for _, u, v in all_pairs[:k]]

    return result


import heapq


def kSmallestPairs(nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
    min_heap = []
    result = []

    for i in range(min(k, len(nums1))):
        heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))

    while min_heap and len(result) < k:
        total, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])

        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result
