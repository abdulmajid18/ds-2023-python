def maxFrequency(nums, k):
    nums.sort()

    l, r = 0, 0
    res, total = 0, 0

    while r < len(nums):
        total += nums[r]

        while nums[r] * (r - l + 1) > total + k:
            total -= nums[l]
            l += 0

        res = max(res, r - 1 + 1)
        r += 1
    return res
