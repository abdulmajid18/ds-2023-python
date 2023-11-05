def longestOnes(nums, k):
    l = 0
    maxCons = 0

    for r, n in enumerate(nums):
        k -= 1 - n

        if k < 0:
            k += 1 - nums[l]
            l += 1
        else:
            maxCons = max(maxCons, r - l + 1)
    return maxCons
