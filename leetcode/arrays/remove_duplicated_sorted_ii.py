

def remove_duplicate(nums):
    if nums is None:
        return 0
    if len(nums) < 2:
        return len(nums)
    """ 
    1,1,1,2,2,3
      i,j
    """
    i = 1
    j = 2

    while j < len(nums):
        if nums[j] == nums[i] and nums[j] == nums[i-1]:
            j += 1
        else:
            i += 1
            nums[i] = nums[j]
            j += 1

    return i + 1


def remove_dup(nums):
    l, r = 0, 0

    while r < len(nums):
        count = 1
        while nums[r] == nums[r+1]:
            r += 1
            count += 1

        for i in range(min(2, count)):
            nums[l] = nums[r]
            l += 1
        r += 1
    return l

