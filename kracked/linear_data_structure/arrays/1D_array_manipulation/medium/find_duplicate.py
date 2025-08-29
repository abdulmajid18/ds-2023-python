from typing import List


def findDuplicateSorting(nums: List[int]) -> int:

    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]
    return None


def findDuplicateFloyds(nums: List[int]) -> int:
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow