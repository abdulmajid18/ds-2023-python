import heapq
import heapq


def kSmallestPairs(nums1, nums2, k):
    if not nums1 or not nums2:
        return []

    result = []
    min_heap = [(nums1[0] + nums2[0], 0, 0)]

    while min_heap and len(result) < k:
        sum_val, i, j = heapq.heappop(min_heap)
        result.append([nums1[i], nums2[j]])

        if i + 1 < len(nums1):
            heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
        if j + 1 < len(nums2) and i == 0:
            heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return result
