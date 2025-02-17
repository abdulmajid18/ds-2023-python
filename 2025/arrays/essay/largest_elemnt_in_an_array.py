def findMax(nums):
    # Sort the array in ascending order
    nums.sort()

    # Return the last element in the sorted array
    return nums[-1]


def findMax2(nums):
    # Initialize max variable
    max_element = nums[0]

    # Iterate through the array to find the largest element
    for num in nums:
        if num > max_element:
            max_element = num

    return max_element
