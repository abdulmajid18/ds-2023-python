from typing import List


def productExceptSelfBrute(nums: List[int]) -> List[int]:
    n = len(nums)
    res = []

    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        res.append(prod)

    return res


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n

    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]


    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]

    return res