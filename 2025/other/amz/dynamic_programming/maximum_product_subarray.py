from typing import List


def maxProductBruteForce(nums: List[int]) -> int:
    n = len(nums)
    max_product = float('-inf')

    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            max_product = max(max_product, product)

    return max_product


def maxProductOptimal(nums: List[int]) -> int:
    res = max(nums)  # Initialize result with the largest single number
    curMin, curMax = 1, 1  # Start min and max product as 1

    for n in nums:
        # Swap curMax and curMin if n is negative
        if n < 0:
            curMax, curMin = curMin, curMax

        # Update curMax and curMin
        curMax = max(n * curMax, n)
        curMin = min(n * curMin, n)

        # Update the result
        res = max(res, curMax)

    return res