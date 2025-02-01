def removeDuplicates(nums):
    if not nums:
        return 0  #

    left = 1
    for right in range(2, len(nums)):
        if nums[right] != nums[left] or nums[right] != nums[left - 1]:
            left += 1
            nums[left] = nums[right]
    return left + 1
