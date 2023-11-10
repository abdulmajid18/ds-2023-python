def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0  # No subarray can have a product less than or equal to 1.

    count = 0
    product = 1
    left = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k:
            product /= nums[left]
            left += 1

        # At this point, any subarray starting at 'left' and ending at 'right' is valid.
        # Count the subarrays ending at 'right'.
        count += (right - left + 1)

    return count

# Example usage:
nums = [10, 5, 2, 6]
k = 100
result = numSubarrayProductLessThanK(nums, k)
print(result)  # This will output 8 for the example array.
