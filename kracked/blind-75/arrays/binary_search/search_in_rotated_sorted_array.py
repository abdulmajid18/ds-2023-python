def search_rotated(nums, target):
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if target == nums[mid]:
            return mid

        #  check the left portion
        if nums[l] <= nums[mid]:
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # check the right portion
        else:
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[r]:
                r = mid -1
            else:
                l = mid + 1
    return -1



