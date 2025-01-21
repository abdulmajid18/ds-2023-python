from typing import List

from typing import List


def maxProductSubArray(nums: List[int]) -> int:
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


#  use this quite intuitive
def maxProductSubArray2(nums: List[int]) -> int:
    res = max(nums)
    curMin, curMax = 1, 1

    for n in nums:
        if n == 0:
            curMin, curMax = 1, 1
            continue
        tmp = curMax * n
        curMax = max(n * curMax, n * curMin, n)
        curMin = min(tmp, n * curMin, n)
        res = max(curMax, res)
    return res


def maxProduct(nums):
    if not nums:
        return 0

    # Initialize variables
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    # Iterate through the array
    for i in range(1, len(nums)):
        num = nums[i]

        # If the current number is negative, swap max_product and min_product
        if num < 0:
            max_product, min_product = min_product, max_product

        # Update max_product and min_product
        max_product = max(num, num * max_product)
        min_product = min(num, num * min_product)

        # Update the result
        result = max(result, max_product)

    return result


def maxProductBruteForce(nums):
    n = len(nums)
    max_product = float('-inf')  # Initialize to negative infinity

    # Iterate through all possible subarrays
    for i in range(n):
        product = 1  # Reset product for each new starting point
        for j in range(i, n):
            product *= nums[j]  # Compute product of subarray nums[i:j+1]
            max_product = max(max_product, product)  # Update max product

    return max_product
