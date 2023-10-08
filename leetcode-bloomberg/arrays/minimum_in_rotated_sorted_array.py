def minimum_rotated_1(elements):
    l = 0
    r = len(elements)

    while l < r and elements[l] >= elements[r]:
        m = (l + r) // 2
        if elements[r] < elements[m]:
            l = m + 1
        else:
            r = m
    return elements[l]


def minimum_rotated_2(nums):
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:
            l = m + 1
        else:
            r = m - 1
    return res
