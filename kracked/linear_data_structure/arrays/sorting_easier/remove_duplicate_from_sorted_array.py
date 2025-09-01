from typing import List


def removeDuplicates(nums: List[int]) -> int:
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

    i = 0  # slow pointer
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]

    return i + 1


