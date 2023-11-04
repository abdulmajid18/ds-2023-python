def squares_of_sorted(nums):
    res = []
    l = 0
    r = len(nums) - 1

    while l < r:
        if nums[l] * nums[l] > nums[r] * nums[r]:
            res.append(nums[l] * nums[l])
            l += 1
        else:
            res.append(nums[r] * nums[r])
            r -= 1




    return res[::1]