from typing import List

def pair_sum_sorted_brute_force(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []



def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1

    while left < right:
        sum_ = nums[left] + nums[right]

        if sum_ < target:
            left += 1
        elif sum_ > target:
            right -= 1
        else:
            return [left, right]  # pair found

    return []  # no pair found
