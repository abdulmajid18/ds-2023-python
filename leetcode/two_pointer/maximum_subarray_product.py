def maximum_product_subarray(nums):
    res = max(nums)
    cur_max = 1
    cur_min = 1

    # cur_min, cur_max, res could be the first element in the array

    for n in nums:
        if n == 0:
            cur_max = 1
            cur_min = 1
            continue
        temp = cur_max
        #  we consider adding n to the max and min because we could have [-1,8]
        cur_max = max(n * cur_max, n * cur_min, n)
        cur_min = min(n * temp, n * cur_min, n)  # [-1,-8]
        res = max(cur_max, cur_min)
    return res


import sys


# Returns the product of max product subarray.
def maxSubarrayProduct(arr, n):
    ans = -sys.maxsize - 1  # Initialize the answer to the minimum possible value
    product = 1

    for i in range(n):
        product *= arr[i]
        ans = max(ans, product)  # Update the answer with the maximum of the current answer and product
        if arr[i] == 0:
            product = 1  # Reset the product to 1 if the current element is 0

    product = 1

    for i in range(n - 1, -1, -1):
        product *= arr[i]
        ans = max(ans, product)
        if arr[i] == 0:
            product = 1

    return ans


def maxProductTwoPointers(nums):
    if not nums:
        return 0

    max_product = float("-inf")
    left_max = right_max = 1

    left, right = 0, len(nums) - 1

    # Iterate from left to right
    while left < len(nums):
        left_max *= nums[left]
        max_product = max(max_product, left_max)
        if left_max == 0:
            left_max = 1
        left += 1

    # Reset left_max and iterate from right to left
    left_max = 1

    while right >= 0:
        right_max *= nums[right]
        max_product = max(max_product, right_max)
        if right_max == 0:
            right_max = 1
        right -= 1

    return max_product




def maxSubarrayProduct(arr):
    # Store the result that is the max we have found so far
    r = arr[0]

    # imax/imin store the max/min product of subarray that ends
    # with the current number arr[i]
    imax = r
    imin = r

    for i in range(1, len(arr)):
        # Multiplied by a negative makes a big
        # number smaller and a small number bigger
        # So we redefine the extremums by swapping them
        if arr[i] < 0:
            imax, imin = imin, imax

        # Max/min product for the current number is
        # either the current number itself
        # or the max/min by the previous number times the current one
        imax = max(arr[i], imax * arr[i])
        imin = min(arr[i], imin * arr[i])

        # The newly computed max value is a candidate
        # for our global result
        r = max(r, imax)

    return r


def maxProduct4(nums):
    if not nums:
        return 0

    # Initialize variables to keep track of the maximum and minimum product ending at the current element.
    max_ending_here = min_ending_here = max_so_far = nums[0]

    for i in range(1, len(nums)):
        # Swap max_ending_here and min_ending_here if the current element is negative.
        if nums[i] < 0:
            max_ending_here, min_ending_here = min_ending_here, max_ending_here

        # Update max_ending_here and min_ending_here based on the current element.
        max_ending_here = max(nums[i], max_ending_here * nums[i])
        min_ending_here = min(nums[i], min_ending_here * nums[i])

        # Update max_so_far with the maximum value seen so far.
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far



