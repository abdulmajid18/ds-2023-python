from typing import List

from typing import List


def searchRangeBruteForce(nums: List[int], target: int) -> List[int]:
    start, end = -1, -1

    for i in range(len(nums)):
        if nums[i] == target:
            if start == -1:
                start = i
            end = i  # keep updating end as long as target matches

    return [start, end]


from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def find_first(nums, target):
        l, r = 0, len(nums)-1
        first = -1
        while l <= r:
            mid = (r+l) // 2
            if nums[mid] == target:
                r = mid - 1
                first = mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return first

    def find_second(nums, target):
        l, r = 0, len(nums)-1
        second = -1
        while l <= r:
            mid = (r+l) // 2
            if nums[mid] == target:
                l = mid + 1
                second = mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return second

    first = find_first(nums, target)
    last = find_second(nums, target)

    return [first, last]

