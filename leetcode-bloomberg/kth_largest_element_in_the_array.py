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
