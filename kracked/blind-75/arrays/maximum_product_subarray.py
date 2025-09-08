from typing import List


def maxProductBruteForce(nums: List[int]) -> int:
    n = len(nums)
    ans = nums[0]

    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= nums[j]
            ans = max(ans, product)

    return ans


def maxProduct(nums: List[int]) -> int:
    res = max(nums)
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

