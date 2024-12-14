def three_sum(nums):
    res = []
    nums.sort()

    for i, v in enumerate(nums):
        if i > 0 and v == nums[i-1]:
            continue

        l, r = i + 1, len(nums)-1
        while l < r:
            threeSum = v + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([v, nums[l], nums[r]])
