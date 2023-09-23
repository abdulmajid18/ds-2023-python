def remove(nums, a):
    i = 0
    j = 0

    while j < len(nums):
        if nums[j] != a:
            nums[i] = nums[j]
            i += 1
        j += 1
    return i