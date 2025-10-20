from typing import List


def removeDuplicatesOne(nums: List[int]) -> int:
    l, r = 0, 1
    n = len(nums)
    while r < n:
        if nums[l] != nums[r]:
            l += 1
            nums[l] = nums[r]
        r += 1
    return l + 1



def removeDuplicatesTwo(nums: List[int]) -> int:
    if not nums:
        return 0

    l = 0
    for r in range(1, len(nums)):
        if nums[r] != nums[l]:
            l += 1
            nums[l] = nums[r]

    return l + 1


