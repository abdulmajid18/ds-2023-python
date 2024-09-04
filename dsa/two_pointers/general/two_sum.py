from typing import List


def two_sum_brute_force(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None


def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return i, j


def twoSumMap(self, nums: List[int], target: int) -> List[int]:
    hash_map = {}
    for k, v in enumerate(nums):
        expected_num = target - v
        if expected_num in hash_map:
            return hash_map[expected_num], k
        else:
            hash_map[v] = k
