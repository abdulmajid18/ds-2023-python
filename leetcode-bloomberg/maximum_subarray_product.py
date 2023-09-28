def maximum_product_subarray(nums):
    res = max(nums)
    cur_max = 1
    cur_min = 1

    # cur_min, cur_max, res could be the first element in the array

    for n in nums:
        if n == 0:
            cur_max = 1
            cur_min = 1
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



# Driver code
arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print("Maximum Subarray product is", maxSubarrayProduct(arr, n))


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


arr = [1, -2, -3, 0, 7, -8, -2]
print("Maximum Subarray Product is", maxSubarrayProduct(arr))