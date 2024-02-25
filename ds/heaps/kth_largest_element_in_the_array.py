def find_kth_latgest_1(nums, k):
    nums.sort()
    return nums[len(nums)-k]


def find_kth_largest_two(nums, k):
    k = len(nums) - k

    def quick_select(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            quick_select(l, p-1)
        elif p < k:
            quick_select(p+1, r)
        else:
            return nums[p]

    return quick_select(0, len(nums) - 1)


import heapq


def kth_largest(nums, k):
    # Build a min-heap containing the first k elements
    min_heap = nums[:k]
    heapq.heapify(min_heap)

    # Process remaining elements in the array
    for num in nums[k:]:
        if num > min_heap[0]:
            # Replace the root with the current element
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    # Return the kth largest element
    return min_heap[0]


# Example usage:
nums = [3, 2, 1, 5, 6, 4]
k = 2
print("The", k, "largest element is:", kth_largest(nums, k))
