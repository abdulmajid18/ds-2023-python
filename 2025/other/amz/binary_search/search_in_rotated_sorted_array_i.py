from typing import List


def searchBruteForce(nums: List[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


from typing import List


def searchOptimalOne(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        # left sorted partition
        if nums[left] <= nums[mid]:
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[right]:
                right = mid - 1
            else:
                left = mid + 1

    return -1


from typing import List


def searchOptimalTwo(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = l + (r - l) // 2

        if nums[mid] == target:
            return mid

        if nums[l] <= nums[mid]:
            #  check if we use the current left window or move to the right sorted
            if target >= nums[l]:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                l = mid + 1
        else:
            if target <= nums[r]:
                if target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                r = mid - 1

    return -1  # Target not found
