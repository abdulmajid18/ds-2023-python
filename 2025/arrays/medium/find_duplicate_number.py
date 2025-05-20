from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        bucket = [0] * (n + 1)
        print(bucket)

        for num in nums:
            if bucket[num] == 1:
                return num
            bucket[num] += 1


def findDuplicate(nums):
    count_map = {}
    for num in nums:
        if num in count_map:
            return num
        count_map[num] = 1


def findDuplicateFloyd(nums: List[int]) -> int:
    slow = 0
    fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
