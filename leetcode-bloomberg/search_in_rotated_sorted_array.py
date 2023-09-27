def search_rotated_array(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        m = (l + r) // 2
        if target == nums[m]:
            return m

        if nums[l] <= nums[m]:
            if target > nums[m]:
                l = m + 1
            elif target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        else:
            if target < nums[m]:
                r = m - 1
            elif target > nums[r]:
                r = m - 1
            else:
                l = m + 1
    return -1