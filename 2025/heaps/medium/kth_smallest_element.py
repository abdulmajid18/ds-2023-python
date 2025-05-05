def kth_smallest_sort(nums, k):
    nums.sort()
    return nums[k - 1]


import heapq


def kth_smallest_heap(nums, k):
    heapq.heapify(nums)
    for _ in range(k - 1):
        heapq.heappop(nums)
    return heapq.heappop(nums)


def kth_smallest_quickselect(nums, k):
    k -= 1

    def quickselect(left, right):
        if left == right:
            return nums[left]

        pivot = nums[right]
        p = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[i], nums[p] = nums[p], nums[i]
                p += 1
        nums[p], nums[right] = nums[right], nums[p]

        if p == k:
            return nums[p]
        elif k < p:
            return quickselect(left, p - 1)
        else:
            return quickselect(p + 1, right)

    return quickselect(0, len(nums) - 1)
