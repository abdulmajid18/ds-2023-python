from typing import List


def missingNumber(nums: List[int]) -> int:
    missing_num = 0

    for i in range(len(nums) + 1):
        missing_num ^= i

    for num in nums:
        missing_num ^= num

    return missing_num



def missingNumberSet(nums: List[int]) -> int:
    num_set = set(nums)   # store all numbers
    n = len(nums)

    for i in range(n + 1):
        if i not in num_set:
            return i
    return None

